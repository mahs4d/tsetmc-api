from jdatetime import date as jdate
from pydantic import BaseModel


class SymbolTradersTypeSubInfo(BaseModel):
    count: int
    volume: int
    value: int


class SymbolTradersTypeInfo(BaseModel):
    buy: SymbolTradersTypeSubInfo
    sell: SymbolTradersTypeSubInfo


class SymbolTradersTypeDataRow(BaseModel):
    date: jdate
    legal: SymbolTradersTypeInfo
    real: SymbolTradersTypeInfo

    class Config:
        arbitrary_types_allowed = True
