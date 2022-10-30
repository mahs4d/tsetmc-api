from jdatetime import date as jdate
from pydantic import BaseModel

from . import _core


class DayDetailsShareHolderPortfolioRow(BaseModel):
    symbol_id: str
    short_name: str
    long_name: str


class DayDetailsShareHolder(BaseModel):
    id: str
    name: str

    def get_portfolio_data(self) -> list[DayDetailsShareHolderPortfolioRow]:
        """
        returns list of companies owned by this shareholder
        """

        raw_data = _core.get_shareholder_portfolio(shareholder_id=self.id)

        return [DayDetailsShareHolderPortfolioRow(
            symbol_id=row['symbol_id'],
            short_name=row['short_name'],
            long_name=row['long_name'],
        ) for row in raw_data]


class DayDetailsShareHolderChartRow(BaseModel):
    date: jdate
    count: int
    percentage: float


class DayDetailsShareHolderDataRow(BaseModel):
    symbol_id: str
    date: jdate
    shareholder: DayDetailsShareHolder
    count: int
    percentage: float

    def get_chart_data(self, days: int = 90) -> list[DayDetailsShareHolderChartRow]:
        """
        returns list of changes to shareholders share count in history of this symbol
        """

        raw_data = _core.get_shareholder_chart_data(
            symbol_id=self.symbol_id,
            shareholder_id=self.shareholder.id,
            days=days,
        )

        return [DayDetailsShareHolderChartRow(
            date=row['date'],
            count=row['count'],
            percentage=row['percentage'],
        ) for row in raw_data]

    class Config:
        arbitrary_types_allowed = True
