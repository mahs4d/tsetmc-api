from pydantic import BaseModel


class TradersTypeSubData(BaseModel):
    count: int
    volume: int
    value: int


class TradersTypeData(BaseModel):
    buy: TradersTypeSubData
    sell: TradersTypeSubData


class TradersTypeRow(BaseModel):
    legal: TradersTypeData
    real: TradersTypeData
