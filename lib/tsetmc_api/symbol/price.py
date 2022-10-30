from jdatetime import date as jdate
from jdatetime import time as jtime
from pydantic import BaseModel

from .group import SymbolGroupDataRow
from .orderbook import SymbolOrderBookData
from .traders_type import SymbolTradersTypeDataRow


class SymbolPriceData(BaseModel):
    last: int
    close: int
    open: int
    yesterday: int
    high: int
    low: int
    count: int
    volume: int
    value: int


class SymbolDailyPriceDataRow(SymbolPriceData):
    date: jdate

    class Config:
        arbitrary_types_allowed = True


class SymbolPriceOverview(BaseModel):
    price_data: SymbolPriceData
    orderbook: SymbolOrderBookData
    traders_type: SymbolTradersTypeDataRow
    group_data: list[SymbolGroupDataRow]


class SymbolIntraDayPriceChartDataRow(BaseModel):
    time: jtime
    high: int
    low: int
    open: int
    close: int
    volume: int

    class Config:
        arbitrary_types_allowed = True
