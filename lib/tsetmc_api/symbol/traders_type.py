from pydantic import BaseModel


class SymbolTradersTypeSubInfo(BaseModel):
    count: int
    volume: int
    value: int


class SymbolTradersTypeInfo(BaseModel):
    buy: SymbolTradersTypeSubInfo
    sell: SymbolTradersTypeSubInfo


class SymbolTradersTypeDataRow(BaseModel):
    legal: SymbolTradersTypeInfo
    real: SymbolTradersTypeInfo
