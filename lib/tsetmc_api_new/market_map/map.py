from enum import Enum

from pydantic import BaseModel

from . import _core


class MapTickRow(BaseModel):
    symbol_id: str
    symbol_short_name: str
    symbol_long_name: str

    close: int
    last: int
    volume: int
    value: int
    count: int

    group_name: str

    color: str
    price_change_percent: float
    percent: float


class MapType(Enum):
    MARKET_VALUE = 1
    MARKET_VOLUME = 2


class MarketMap:
    def get_market_map_tick(self, map_type: MapType = MapType.MARKET_VALUE) -> list[MapTickRow]:
        """
        returns symbol data in market map (in "naghshe bazar" page)
        !!! webserver occasionally throws 403 error, you should retry in a few seconds when this happens
        """

        raw_data = _core.get_market_map_data(map_type=map_type.value)

        rows = [MapTickRow(
            symbol_id=row['symbol_id'],
            symbol_short_name=row['symbol_short_name'],
            symbol_long_name=row['symbol_long_name'],

            close=row['close'],
            last=row['last'],
            volume=row['volume'],
            value=row['value'],
            count=row['count'],

            group_name=row['group_name'],

            color=row['color'],
            price_change_percent=row['price_change_percent'],
            percent=row['percent'],
        ) for row in raw_data]

        return rows
