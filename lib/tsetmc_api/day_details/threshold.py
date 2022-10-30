from pydantic import BaseModel


class DayDetailsThresholdsData(BaseModel):
    range_max: int
    range_min: int
