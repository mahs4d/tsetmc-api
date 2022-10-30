from pydantic import BaseModel


class WatchDailyHistoryDataRow(BaseModel):
    day: int
    open: int
    close: int
    last: int
    count: int
    volume: int
    value: int
    low: int
    high: int
    yesterday: int
