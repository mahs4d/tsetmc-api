from pydantic import BaseModel


class WatchOrderBookRow(BaseModel):
    count: int
    price: int
    volume: int


class WatchOrderBook(BaseModel):
    buy_rows: list[WatchOrderBookRow]
    sell_rows: list[WatchOrderBookRow]
