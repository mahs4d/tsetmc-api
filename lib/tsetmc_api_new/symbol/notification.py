from jdatetime import datetime as jdatetime
from pydantic import BaseModel


class Notification(BaseModel):
    datetime: jdatetime
    title: str

    class Config:
        arbitrary_types_allowed = True
