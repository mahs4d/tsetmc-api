from pydantic import BaseModel


class WatchTradersTypeSubData(BaseModel):
    count: int
    volume: int


class WatchTradersTypeData(BaseModel):
    buy: WatchTradersTypeSubData
    sell: WatchTradersTypeSubData


class WatchTradersTypeRow(BaseModel):
    legal: WatchTradersTypeData
    real: WatchTradersTypeData
