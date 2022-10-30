from jdatetime import time as jtime
from pydantic import BaseModel


class DayDetailsPriceDataRow(BaseModel):
    time: jtime
    close: int
    last: int
    value: int
    volume: int
    count: int

    class Config:
        arbitrary_types_allowed = True


class DayDetailsPriceOverview(BaseModel):
    price_change: int
    low: int
    high: int
    yesterday: int
    open: int
    close: int
    last: int
    count: int
    volume: int
    value: int
