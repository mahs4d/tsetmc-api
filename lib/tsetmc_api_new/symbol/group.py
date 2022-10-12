from pydantic import BaseModel


class GroupDataRow(BaseModel):
    symbol_id: str
    last: int
    close: int
    count: int
    volume: int
    value: int
