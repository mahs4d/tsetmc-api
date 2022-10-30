from jdatetime import time as jtime
from pydantic import BaseModel


class DayDetailsTradeDataRow(BaseModel):
    time: jtime
    price: int
    volume: int

    class Config:
        arbitrary_types_allowed = True
