import time
from abc import ABC, abstractmethod
from traceback import print_exc
from typing import List, Optional

import schedule

from .core import watch as watch_core


class WatchTick:
    def __init__(self,
                 price_data: dict,
                 client_type_data: dict,
                 historical_data: Optional[List[dict]],
                 stats_data: Optional[dict]):
        self.price_data = price_data
        self.client_type_data = client_type_data
        self.historical_data = historical_data
        self.stats_data = stats_data

    def get_symbol_ids(self) -> List[str]:
        """
        لیست آی دی همه‌ی نمادهای داخل دیده‌بان
        """
        return list(self.price_data.keys())

    def get_price_data(self, symbol_id) -> dict:
        """
        اطلاعات قیمتی و سفارشات دیده‌بان
        """
        return self.price_data.get(symbol_id, {})

    def get_client_type_data(self, symbol_id) -> dict:
        """
        اطلاعات حقیقی حقوقی دیده‌بان
        """
        return self.client_type_data.get(symbol_id, {})

    def get_historical_data(self, symbol_id) -> Optional[dict]:
        """
        اطلاعات سابقه‌ی دیده‌بان
        """
        if self.historical_data is None:
            return None

        return self.historical_data.get(symbol_id, {})

    def get_stats_data(self, symbol_id) -> Optional[dict]:
        """
        آمارهای کلیدی دیده‌بان
        """
        if self.stats_data is None:
            return None

        return self.stats_data.get(symbol_id, {})


class Filter(ABC):
    @abstractmethod
    def apply(self, symbol_id: str, watch_tick: WatchTick) -> bool:
        pass

    def __and__(self, other):
        me = self

        class AndFilter(Filter):
            def apply(self, symbol_id: str, watch_tick: WatchTick):
                return me.apply(symbol_id, watch_tick) and other.apply(symbol_id, watch_tick)

        return AndFilter()

    def __or__(self, other):
        me = self

        class OrFilter(Filter):
            def apply(self, symbol_id: str, watch_tick: WatchTick):
                return me.apply(symbol_id, watch_tick) or other.apply(symbol_id, watch_tick)

        return OrFilter()

    def __invert__(self):
        me = self

        class InvertedFilter(Filter):
            def apply(self, symbol_id: str, watch_tick: WatchTick):
                return not me.apply(symbol_id, watch_tick)

        return InvertedFilter()


class Watch:
    def __init__(self,
                 simple_refresh_time: int = 1,
                 client_type_refresh_time: int = 60,
                 historical_data: bool = True,
                 stats_data: bool = True,
                 ):
        self._price_data_rtime = simple_refresh_time
        self._client_type_data_rtime = client_type_refresh_time
        self._historical_data = historical_data
        self._stats_data = stats_data

        self._last_price_data = None
        self._last_client_type_data = None
        self._last_historical_data = None
        self._last_stats_data = None
        self._last_tick = None
        self._bindings = []

    def bind_listener(self, listener, filter_instance: Filter = None):
        self._bindings.append({
            'listener': listener,
            'filter': filter_instance,
        })

        return self

    def prepare_watch(self):
        """
        کنترل دستی
        """
        if self._historical_data:
            while self._last_historical_data is None:
                self._update_historical_data()

        if self._stats_data:
            while self._last_stats_data is None:
                self._update_stats_data()

        while self._last_price_data is None:
            self._update_price_data()

        while self._last_client_type_data is None:
            self._update_client_type_data()

        schedule.every(self._price_data_rtime).seconds.do(self._update_price_data)
        schedule.every(self._client_type_data_rtime).seconds.do(self._update_client_type_data)

    def step_watch(self):
        """
        کنترل دستی
        """
        try:
            schedule.run_pending()
            time.sleep(1)
        except:
            print_exc()

    def start_watch(self):
        """
        شروع دیده‌بان
        """
        self.prepare_watch()
        while True:
            self.step_watch()

    def _publish(self):
        if self._historical_data:
            if self._last_historical_data is None:
                return

        if self._stats_data:
            if self._last_stats_data is None:
                return

        if self._last_price_data is None:
            return

        if self._last_client_type_data is None:
            return

        self._last_tick = WatchTick(price_data=self._last_price_data,
                                    client_type_data=self._last_client_type_data,
                                    historical_data=self._last_historical_data,
                                    stats_data=self._last_stats_data, )

        for binding in self._bindings:
            if binding['filter'] is None:
                binding['listener'](self._last_tick)
            else:
                binding['listener'](_create_filtered_tick(self._last_tick, binding['filter']))

    def _update_price_data(self):
        try:
            self._last_price_data, _ = watch_core.fetch_watch_price_data()
        except:
            print_exc()
            return

        self._publish()

    def _update_client_type_data(self):
        try:
            self._last_client_type_data = watch_core.fetch_watch_client_type_data()
        except Exception as ex:
            print_exc()
            return

        self._publish()

    def _update_historical_data(self):
        try:
            self._last_historical_data = watch_core.fetch_watch_historical_data()
        except:
            print_exc()

    def _update_stats_data(self):
        try:
            self._last_stats_data = watch_core.fetch_watch_stats_data()
        except:
            print_exc()


class SahamFilter(Filter):
    def apply(self, symbol_id: str, watch_tick: WatchTick) -> bool:
        yval = watch_tick.get_price_data(symbol_id=symbol_id).get('yval')
        return yval in [300, 303, 313]


class PayeFarabourseFilter(Filter):
    def apply(self, symbol_id: str, watch_tick: WatchTick) -> bool:
        yval = watch_tick.get_price_data(symbol_id=symbol_id).get('yval')
        return yval in [309]


class HaghTaghaddomFilter(Filter):
    def apply(self, symbol_id: str, watch_tick: WatchTick) -> bool:
        yval = watch_tick.get_price_data(symbol_id=symbol_id).get('yval')
        return yval in [400, 403, 404]


class OraghMosharekatFilter(Filter):
    def apply(self, symbol_id: str, watch_tick: WatchTick) -> bool:
        yval = watch_tick.get_price_data(symbol_id=symbol_id).get('yval')
        return yval in [306, 301, 706, 208]


class AtiFilter(Filter):
    def apply(self, symbol_id: str, watch_tick: WatchTick) -> bool:
        yval = watch_tick.get_price_data(symbol_id=symbol_id).get('yval')
        return yval in [263]


class SandoghFilter(Filter):
    def apply(self, symbol_id: str, watch_tick: WatchTick) -> bool:
        yval = watch_tick.get_price_data(symbol_id=symbol_id).get('yval')
        return yval in [305, 380]


class EkhtiarForoushFilter(Filter):
    def apply(self, symbol_id: str, watch_tick: WatchTick) -> bool:
        yval = watch_tick.get_price_data(symbol_id=symbol_id).get('yval')
        return yval in [600, 602, 605, 311, 312]


class KalaForoushFilter(Filter):
    def apply(self, symbol_id: str, watch_tick: WatchTick) -> bool:
        yval = watch_tick.get_price_data(symbol_id=symbol_id).get('yval')
        return yval in [308, 701]


def _create_filtered_tick(watch_tick: WatchTick, filter_instance: Filter):
    price_data = {}
    historical_data = {}
    stats_data = {}
    client_type_data = {}
    for symbol_id in watch_tick.get_symbol_ids():
        if filter_instance.apply(symbol_id, watch_tick):
            price_data[symbol_id] = watch_tick.get_price_data(symbol_id)
            client_type_data[symbol_id] = watch_tick.get_client_type_data(symbol_id)
            historical_data[symbol_id] = watch_tick.get_historical_data(symbol_id)
            stats_data[symbol_id] = watch_tick.get_stats_data(symbol_id)

    return WatchTick(price_data=price_data,
                     client_type_data=client_type_data,
                     historical_data=historical_data,
                     stats_data=stats_data)
