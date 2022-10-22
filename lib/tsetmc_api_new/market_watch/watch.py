from pydantic import BaseModel
from pydantic.utils import deep_update

from . import _core
from .daily_history import WatchDailyHistoryTick
from .orderbook import WatchOrderBook, WatchOrderBookRow
from .traders_type import WatchTradersTypeData, WatchTradersTypeRow, WatchTradersTypeSubData


class WatchPriceData(BaseModel):
    symbol_id: str
    isin: str
    short_name: str
    full_name: str
    heven: int
    open: int
    close: int
    last: int
    count: int
    volume: int
    value: int
    low: int
    high: int
    yesterday: int
    eps: int
    base_volume: int
    visit_count: int
    flow: int
    group: int
    range_max: int
    range_min: int
    z: int
    yval: int
    orderbook: WatchOrderBook


class MarketWatch:
    def __init__(self):
        self._heven = 0
        self._refid = 0
        self._last_price_data = {}

    def get_price_data(self) -> dict[str, WatchPriceData]:
        """
        gets basic price information (in "didbane bazar" page)
        """

        raw_data, new_refid, new_heven, = _core.get_watch_price_data(refid=self._refid, heven=self._heven)

        self._last_price_data = deep_update(self._last_price_data, raw_data)

        watch_data = {}
        for symbol_id in self._last_price_data.keys():
            data = self._last_price_data[symbol_id]

            watch_data[symbol_id] = WatchPriceData(
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
                    ) for row in data['orderbook']['buy_rows']],
                    sell_rows=[WatchOrderBookRow(
                        count=row['count'],
                        price=row['price'],
                        volume=row['volume'],
                    ) for row in data['orderbook']['sell_rows']],
                )
            )

        self._heven = new_heven
        self._refid = new_refid

        return watch_data

    def get_traders_type_data(self) -> dict[str, WatchTradersTypeData]:
        """
        gets traders type data (in "didebane bazar" page)
        """

        raw_data = _core.get_watch_traders_type_data()

        watch_data = {key: WatchTradersTypeRow(
            legal=WatchTradersTypeData(
                buy=WatchTradersTypeSubData(
                    count=data['legal']['buy']['count'],
                    volume=data['legal']['buy']['volume'],
                ),
                sell=WatchTradersTypeSubData(
                    count=data['legal']['sell']['count'],
                    volume=data['legal']['sell']['volume'],
                ),
            ),
            real=WatchTradersTypeData(
                buy=WatchTradersTypeSubData(
                    count=data['real']['buy']['count'],
                    volume=data['real']['buy']['volume'],
                ),
                sell=WatchTradersTypeSubData(
                    count=data['real']['sell']['count'],
                    volume=data['real']['sell']['volume'],
                ),
            ),
        ) for key, data in raw_data.items()}

        return watch_data

    def get_daily_ticks_history(self) -> dict[str, list[WatchDailyHistoryTick]]:
        """
        gets 30 day history of symbols (in "didbane bazar" page)
        """

        raw_data = _core.get_watch_traders_type_data()

        watch_data = {}
        for symbol_id in raw_data.keys():
            watch_data[symbol_id] = [WatchDailyHistoryTick(
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
