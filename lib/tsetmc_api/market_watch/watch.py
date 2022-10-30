from . import _core
from .daily_history import WatchDailyHistoryDataRow
from .orderbook import WatchOrderBook, WatchOrderBookRow
from .price import WatchPriceDataRow
from .traders_type import WatchTradersTypeDataRow, WatchTradersTypeInfo, WatchTradersTypeSubInfo
from ..utils import deep_update


class MarketWatch:
    def __init__(self):
        self._heven = 0
        self._refid = 0
        self._last_price_data = {}

    def get_price_data(self) -> dict[str, WatchPriceDataRow]:
        """
        gets basic price information (in "didbane bazar" page)
        """

        raw_data, new_refid, new_heven, = _core.get_watch_price_data(refid=self._refid, heven=self._heven)

        self._last_price_data = deep_update(self._last_price_data, raw_data)

        watch_data = {}
        for symbol_id in self._last_price_data.keys():
            data = self._last_price_data[symbol_id]

            if 'symbol_id' not in data:
                continue

            watch_data[symbol_id] = WatchPriceDataRow(
                symbol_id=data['symbol_id'],
                isin=data['isin'],
                short_name=data['short_name'],
                full_name=data['full_name'],
                heven=data['heven'],
                open=data['open'],
                close=data['close'],
                last=data['last'],
                count=data['count'],
                volume=data['volume'],
                value=data['value'],
                low=data['low'],
                high=data['high'],
                yesterday=data['yesterday'],
                eps=data['eps'],
                base_volume=data['base_volume'],
                visit_count=data['visit_count'],
                flow=data['flow'],
                group=data['group'],
                range_max=data['range_max'],
                range_min=data['range_min'],
                z=data['z'],
                yval=data['yval'],
                orderbook=WatchOrderBook(
                    buy_rows=[WatchOrderBookRow(
                        count=row['count'],
                        price=row['price'],
                        volume=row['volume'],
                    ) for row in data['orderbook']['buy_rows'].values()],
                    sell_rows=[WatchOrderBookRow(
                        count=row['count'],
                        price=row['price'],
                        volume=row['volume'],
                    ) for row in data['orderbook']['sell_rows'].values()],
                )
            )

        self._heven = new_heven
        self._refid = new_refid

        return watch_data

    def get_traders_type_data(self) -> dict[str, WatchTradersTypeDataRow]:
        """
        gets traders type data (in "didebane bazar" page)
        """

        raw_data = _core.get_watch_traders_type_data()

        watch_data = {}
        for key, data in raw_data.items():
            watch_data[key] = WatchTradersTypeDataRow(
                legal=WatchTradersTypeInfo(
                    buy=WatchTradersTypeSubInfo(
                        count=data['legal']['buy']['count'],
                        volume=data['legal']['buy']['volume'],
                    ),
                    sell=WatchTradersTypeSubInfo(
                        count=data['legal']['sell']['count'],
                        volume=data['legal']['sell']['volume'],
                    ),
                ),
                real=WatchTradersTypeInfo(
                    buy=WatchTradersTypeSubInfo(
                        count=data['real']['buy']['count'],
                        volume=data['real']['buy']['volume'],
                    ),
                    sell=WatchTradersTypeSubInfo(
                        count=data['real']['sell']['count'],
                        volume=data['real']['sell']['volume'],
                    ),
                ),
            )

        return watch_data

    def get_daily_history_data(self) -> dict[str, list[WatchDailyHistoryDataRow]]:
        """
        gets 30 day history of symbols (in "didbane bazar" page)
        """

        raw_data = _core.get_watch_daily_history_data()

        watch_data = {}
        for symbol_id in raw_data.keys():
            watch_data[symbol_id] = [WatchDailyHistoryDataRow(
                day=row['day'],
                open=row['open'],
                close=row['close'],
                last=row['last'],
                count=row['count'],
                volume=row['volume'],
                value=row['value'],
                low=row['low'],
                high=row['high'],
                yesterday=row['yesterday'],
            ) for row in raw_data[symbol_id]]

        return watch_data

    def get_raw_stats_data(self) -> dict[list]:
        """
        returns a list of stats for each symbol. refer to tsetmc.com for information of what each item in the list is
        """

    def get_stats_data(self) -> dict[dict]:
        """
        !!! EXPERIMENTAL: returns stats in dict, may be wrong !!!
        """

        return _core.get_watch_stats_data()
