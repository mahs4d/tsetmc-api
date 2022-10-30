from jdatetime import datetime as jdatetime
from pydantic import BaseModel


class SymbolSupervisorMessageDataRow(BaseModel):
    datetime: jdatetime
    title: str
    content: str

    class Config:
        arbitrary_types_allowed = True
