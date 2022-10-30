from pydantic import BaseModel


class SymbolGroupDataRow(BaseModel):
    symbol_id: str
    last: int
    close: int
    count: int
    volume: int
    value: int
