from pydantic import BaseModel


class DayDetailsTradersTypeSubInfo(BaseModel):
    count: int
    volume: int
    value: int


class DayDetailsTradersTypeInfo(BaseModel):
    buy: DayDetailsTradersTypeSubInfo
    sell: DayDetailsTradersTypeSubInfo


class DayDetailsTradersTypeData(BaseModel):
    legal: DayDetailsTradersTypeInfo
    real: DayDetailsTradersTypeInfo
