import time
from abc import ABC, abstractmethod

import schedule

from .core import watch as watch_core


class WatchTick:
    def __init__(self, simple_data, client_type_data, historical_data, stats_data):
        self.simple_data = simple_data
        self.client_type_data = client_type_data
        self.historical_data = historical_data
        self.stats_data = stats_data

    def get_asset_ids(self):
        """
        لیست آی دی همه‌ی نمادهای داخل دیده‌بان
        """
        return self.simple_data.keys()

    def get_simple_data(self, asset_id):
        """
        اطلاعات قیمتی و سفارشات دیده‌بان
        """
        return self.simple_data.get(asset_id, {})

    def get_client_type_data(self, asset_id):
        """
        اطلاعات حقیقی حقوقی دیده‌بان
        """
        return self.client_type_data.get(asset_id, {})

    def get_historical_data(self, asset_id):
        """
        اطلاعات سابقه‌ی دیده‌بان
        """
        return self.historical_data.get(asset_id, {})

    def get_stats_data(self, asset_id):
        """
        آمارهای کلیدی دیده‌بان
        """
        return self.stats_data.get(asset_id, {})


class Filter(ABC):
    @abstractmethod
    def apply(self, asset_id, watch_tick: WatchTick):
        pass

    def __and__(self, other):
        me = self

        class AndFilter(Filter):
            def apply(self, asset_id, watch_tick):
                return me.apply(asset_id, watch_tick) and other.apply(asset_id, watch_tick)

        return AndFilter()

    def __or__(self, other):
        me = self

        class OrFilter(Filter):
            def apply(self, asset_id, watch_tick):
                return me.apply(asset_id, watch_tick) or other.apply(asset_id, watch_tick)

        return OrFilter()

    def __invert__(self):
        me = self

        class InvertedFilter(Filter):
            def apply(self, asset_id, watch_tick):
                return not me.apply(asset_id, watch_tick)

        return InvertedFilter()


def _create_filtered_tick(watch_tick: WatchTick, filter: Filter):
    simple_data = {}
    historical_data = {}
    stats_data = {}
    client_type_data = {}
    for asset_id in watch_tick.get_asset_ids():
        if filter.apply(asset_id, watch_tick):
            simple_data[asset_id] = watch_tick.get_simple_data(asset_id)
            client_type_data[asset_id] = watch_tick.get_client_type_data(asset_id)
            historical_data[asset_id] = watch_tick.get_historical_data(asset_id)
            stats_data[asset_id] = watch_tick.get_stats_data(asset_id)

    return WatchTick(simple_data=simple_data,
                     client_type_data=client_type_data,
                     historical_data=historical_data,
                     stats_data=stats_data)


class Watch:
    def __init__(self, simple_refresh_time=1, client_type_refresh_time=60):
        self._simple_data_rtime = simple_refresh_time
        self._client_type_data_rtime = client_type_refresh_time

        self._last_simple_data = None
        self._last_client_type_data = None
        self._last_historical_data = None
        self._last_stats_data = None
        self._last_tick = None
        self._bindings = []

    def bind_listener(self, listener, filter: Filter = None):
        self._bindings.append({
            'listener': listener,
            'filter': filter,
        })

        return self

    def start_watch(self):
        """
        شروع دیده‌بان
        """
        while self._last_historical_data is None:
            self._update_historical_data()

        while self._last_stats_data is None:
            self._update_stats_data()

        while self._last_simple_data is None:
            self._update_simple_data()

        while self._last_client_type_data is None:
            self._update_client_type_data()

        schedule.every(self._simple_data_rtime).seconds.do(self._update_simple_data)
        schedule.every(self._client_type_data_rtime).seconds.do(self._update_client_type_data)

        while True:
            schedule.run_pending()
            time.sleep(1)

    def _publish(self):
        if self._last_historical_data is None:
            return

        if self._last_stats_data is None:
            return

        if self._last_simple_data is None:
            return

        if self._last_client_type_data is None:
            return

        self._last_tick = WatchTick(simple_data=self._last_simple_data,
                                    client_type_data=self._last_client_type_data,
                                    historical_data=self._last_historical_data,
                                    stats_data=self._last_stats_data, )

        for binding in self._bindings:
            if binding['filter'] is None:
                binding['listener'](self._last_tick)
            else:
                binding['listener'](_create_filtered_tick(self._last_tick, binding['filter']))

    def _update_simple_data(self):
        try:
            self._last_simple_data, _ = watch_core.fetch_watch_simple_data()
        except:
            print('! error in updating simple data')
            return

        self._publish()

    def _update_client_type_data(self):
        try:
            self._last_client_type_data = watch_core.fetch_watch_client_type_data()
        except Exception as ex:
            print('! error in updating client type data')
            return

        self._publish()

    def _update_historical_data(self):
        try:
            self._last_historical_data = watch_core.fetch_watch_historical_data()
        except:
            print('! error in updating historical data')

    def _update_stats_data(self):
        try:
            self._last_stats_data = watch_core.fetch_watch_stats_data()
        except:
            print('! error in updating stats data')
