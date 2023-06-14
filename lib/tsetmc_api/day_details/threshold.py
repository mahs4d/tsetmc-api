from jdatetime import time as jtime
from pydantic import BaseModel


class DayDetailsThresholdsData(BaseModel):
    time: jtime | None
    range_max: int
    range_min: int

    class Config:
        arbitrary_types_allowed = True
