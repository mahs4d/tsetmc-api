from pydantic import BaseModel


class OrderBookRow(BaseModel):
    count: int
    price: int
    volume: int


class OrderBook(BaseModel):
    buy_rows: list[OrderBookRow]
    sell_rows: list[OrderBookRow]
