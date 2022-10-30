from pydantic import BaseModel


class SymbolOrderBookDataRow(BaseModel):
    count: int
    price: int
    volume: int


class SymbolOrderBookData(BaseModel):
    buy_rows: list[SymbolOrderBookDataRow]
    sell_rows: list[SymbolOrderBookDataRow]
