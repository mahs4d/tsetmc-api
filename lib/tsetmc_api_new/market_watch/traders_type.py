from pydantic import BaseModel


class WatchTradersTypeSubInfo(BaseModel):
    count: int
    volume: int


class WatchTradersTypeInfo(BaseModel):
    buy: WatchTradersTypeSubInfo
    sell: WatchTradersTypeSubInfo


class WatchTradersTypeDataRow(BaseModel):
    legal: WatchTradersTypeInfo
    real: WatchTradersTypeInfo
