from jdatetime import date as jdate
from pydantic import BaseModel


class Tick(BaseModel):
    last: int
    close: int
    open: int
    yesterday: int
    high: int
    low: int
    count: int
    volume: int
    value: int


class DailyTick(Tick):
    date: jdate

    class Config:
        arbitrary_types_allowed = True
