from jdatetime import time as jtime
from pydantic import BaseModel


class DayDetailsOrderBookRow(BaseModel):
    time: jtime
    count: int
    price: int
    volume: int

    class Config:
        arbitrary_types_allowed = True


class DayDetailsOrderBookDataRow(BaseModel):
    time: jtime
    buy_rows: list[DayDetailsOrderBookRow]
    sell_rows: list[DayDetailsOrderBookRow]

    class Config:
        arbitrary_types_allowed = True
