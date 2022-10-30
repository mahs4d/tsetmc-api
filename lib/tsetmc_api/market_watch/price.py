from pydantic import BaseModel

from .orderbook import WatchOrderBook


class WatchPriceDataRow(BaseModel):
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
    eps: int | None
    base_volume: int
    visit_count: int
    flow: int
    group: int
    range_max: int
    range_min: int
    z: int
    yval: int
    orderbook: WatchOrderBook
