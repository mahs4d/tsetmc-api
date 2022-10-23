from pydantic import BaseModel


class WatchDailyHistoryDataRow(BaseModel):
    open: int
    close: int
    last: int
    count: int
    volume: int
    value: int
    low: int
    high: int
    yesterday: int
