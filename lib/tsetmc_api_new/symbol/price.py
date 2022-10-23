from jdatetime import time as jtime
from pydantic import BaseModel

from tsetmc_api_new.symbol.group import GroupDataRow
from tsetmc_api_new.symbol.orderbook import OrderBook
from tsetmc_api_new.symbol.tick import Tick
from tsetmc_api_new.symbol.traders_type import TradersTypeRow


class SymbolPriceOverview(BaseModel):
    tick: Tick
    orderbook: OrderBook
    traders_type: TradersTypeRow
    group_data: list[GroupDataRow]


class SymbolIntraDayPriceChartTick(BaseModel):
    time: jtime
    high: int
    low: int
    open: int
    close: int
    volume: int

    class Config:
        arbitrary_types_allowed = True
