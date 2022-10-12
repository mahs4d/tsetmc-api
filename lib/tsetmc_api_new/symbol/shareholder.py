from jdatetime import date as jdate
from pydantic import BaseModel


class ShareHolderPortfolioRow(BaseModel):
    symbol_id: str
    symbol_name: str
    count: int
    percentage: float


class ShareHolder(BaseModel):
    id: str
    name: str

    def get_portfolio(self) -> list[ShareHolderPortfolioRow]:
        """
        gets symbols that this shareholder is major in them (when you click a row in "saham daran" tab)
        """
        # todo:
        pass


class SymbolShareHolderChangesChartRow(BaseModel):
    count: int
    date: jdate

    class Config:
        arbitrary_types_allowed = True


class SymbolShareHolderRow(BaseModel):
    shareholder: ShareHolder
    count: int
    percentage: float
    change: int

    def get_changes_chart(self) -> list[SymbolShareHolderChangesChartRow]:
        """
        get changes in this shareholders symbol possession (when you click a row in "saham daran" tab)
        """
        # todo
        pass
