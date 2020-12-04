from traceback import print_exc
from typing import Optional, Callable

import schedule

from . import core as watch_core
from .filter import Filter
from .watch_tick import WatchTick, SymbolHistoricalDayData, SymbolClientTypeData, SymbolPriceData, SymbolOrderData


class Watch:
    def __init__(self,
                 price_refresh_rate: int = 1,
                 client_type_refresh_rate: int = 60,
                 load_price_data: bool = True,
                 load_client_type_data: bool = True,
                 load_historical_data: bool = False,
                 load_stats_data: bool = False):
        self.price_refresh_rate = price_refresh_rate
        self.client_type_refresh_rate = client_type_refresh_rate

        self.load_price_data = load_price_data
        self.load_client_type_data = load_client_type_data
        self.load_historical_data = load_historical_data
        self.load_stats_data = load_stats_data

        self._last_price_data = None
        self._last_refid = None
        self._last_min_heven = 0
        self._last_client_type_data = None
        self._last_historical_data = None
        self._last_stats_data = None
        self.last_tick = None
        self._bindings = []

    def bind_listener(self, listener: Callable, filter_instance: Optional[Filter] = None):
        self._bindings.append({
            'listener': listener,
            'filter': filter_instance,
        })

        return self

    def prepare_watch(self):
        """
        کنترل دستی
        """
        if self.load_historical_data:
            while self._last_historical_data is None:
                self._update_historical_data()

        if self.load_stats_data:
            while self._last_stats_data is None:
                self._update_stats_data()

        if self.load_price_data:
            while self._last_price_data is None:
                self._update_price_data()

        if self.load_client_type_data:
            while self._last_client_type_data is None:
                self._update_client_type_data()

        if self.load_price_data:
            schedule.every(self.price_refresh_rate).seconds.do(self._update_price_data)

        if self.load_client_type_data:
            schedule.every(self.client_type_refresh_rate).seconds.do(self._update_client_type_data)

    def step_watch(self):
        """
        کنترل دستی
        """
        try:
            schedule.run_pending()
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
        if self.load_historical_data:
            if self._last_historical_data is None:
                return

        if self.load_stats_data:
            if self._last_stats_data is None:
                return

        if self.load_price_data:
            if self._last_price_data is None:
                return

        if self.load_client_type_data:
            if self._last_client_type_data is None:
                return

        self.last_tick = WatchTick(price_data=self._last_price_data,
                                   client_type_data=self._last_client_type_data,
                                   historical_data=self._last_historical_data,
                                   stats_data=self._last_stats_data,
                                   )

        for binding in self._bindings:
            listener = binding['listener']
            filter = binding['filter']
            if filter is None:
                listener(self.last_tick)
            else:
                filtered_tick = filter.get_filtered_tick(self.last_tick)
                listener(filtered_tick)

    def _update_price_data(self):
        try:
            if self._last_price_data is None:
                raw_price_data, self._last_refid, self._last_min_heven = watch_core.fetch_watch_price_data()
                self._last_price_data = {}
                for symbol in raw_price_data:
                    try:
                        self._last_price_data[symbol] = SymbolPriceData.from_dict(raw_price_data[symbol])
                    except:
                        print_exc()
            else:
                raw_price_updates_data, self._last_refid, self._last_min_heven = watch_core.fetch_watch_price_update_data(
                    min_heven=self._last_min_heven, refid=self._last_refid)
                for symbol in raw_price_updates_data:
                    if symbol not in self._last_price_data:
                        break

                    update_info = raw_price_updates_data[symbol]
                    if update_info.get('open'):
                        self._last_price_data[symbol].heven = update_info.get('heven',
                                                                              self._last_price_data[symbol].heven)
                        self._last_price_data[symbol].open = update_info.get('open', self._last_price_data[symbol].open)
                        self._last_price_data[symbol].close = update_info.get('close',
                                                                              self._last_price_data[symbol].close)
                        self._last_price_data[symbol].last = update_info.get('last', self._last_price_data[symbol].last)
                        self._last_price_data[symbol].high = update_info.get('high', self._last_price_data[symbol].high)
                        self._last_price_data[symbol].low = update_info.get('low', self._last_price_data[symbol].low)
                        self._last_price_data[symbol].count = update_info.get('count',
                                                                              self._last_price_data[symbol].count)
                        self._last_price_data[symbol].volume = update_info.get('volume',
                                                                               self._last_price_data[symbol].volume)
                        self._last_price_data[symbol].value = update_info.get('value',
                                                                              self._last_price_data[symbol].value)

                    if update_info.get('buy_orders'):
                        old_orders = self._last_price_data[symbol].buy_orders
                        for new_order in update_info.get('buy_orders'):
                            for old_order in old_orders:
                                if old_order.rank == new_order.get('rank'):
                                    old_order.count = new_order.get('count')
                                    old_order.price = new_order.get('price')
                                    old_order.volume = new_order.get('volume')
                                    break
                            else:
                                old_orders.append(SymbolOrderData.from_dict(new_order))

                    if update_info.get('sell_orders'):
                        old_orders = self._last_price_data[symbol].sell_orders
                        for new_order in update_info.get('sell_orders'):
                            for old_order in old_orders:
                                if old_order.rank == new_order.get('rank'):
                                    old_order.count = new_order.get('count')
                                    old_order.price = new_order.get('price')
                                    old_order.volume = new_order.get('volume')
                                    break
                            else:
                                old_orders.append(SymbolOrderData.from_dict(new_order))
        except:
            print_exc()
            return

        self._publish()

    def _update_client_type_data(self):
        try:
            raw_client_type_data = watch_core.fetch_watch_client_type_data()
            self._last_client_type_data = {} if self._last_client_type_data is None else self._last_client_type_data
            for symbol in raw_client_type_data:
                self._last_client_type_data[symbol] = SymbolClientTypeData.from_dict(raw_client_type_data[symbol])
        except:
            print_exc()
            return

        self._publish()

    def _update_historical_data(self):
        try:
            raw_historical_data = watch_core.fetch_watch_historical_data()
            self._last_historical_data = {} if self._last_historical_data is None else self._last_historical_data
            for symbol in raw_historical_data.keys():
                self._last_historical_data[symbol] = SymbolHistoricalDayData.from_dict(raw_historical_data[symbol])
        except:
            print_exc()

    def _update_stats_data(self):
        try:
            self._last_stats_data = watch_core.fetch_watch_stats_data()
        except:
            print_exc()
