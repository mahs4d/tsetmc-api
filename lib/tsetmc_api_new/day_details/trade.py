from jdatetime import time as jtime
from pydantic import BaseModel


class DayDetailsTradeDataRow(BaseModel):
    time: jtime
    count: int
    price: int
    volume: int

    class Config:
        arbitrary_types_allowed = True
