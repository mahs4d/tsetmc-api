from jdatetime import date as jdate
from pydantic import BaseModel

from . import _core


class DayDetailsShareHolderPortfolioRow(BaseModel):
    symbol_id: str
    short_name: str
    long_name: str
    shares_count: int
    shares_percent: float


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
            shares_count=row['shares_count'],
            shares_percent=row['shares_percent'],
        ) for row in raw_data]


class DayDetailsShareHolderChartRow(BaseModel):
    date: jdate
    shares_count: int
    shares_percentage: float

    class Config:
        arbitrary_types_allowed = True


class DayDetailsShareHolderDataRow(BaseModel):
    symbol_id: str
    date: jdate
    shareholder: DayDetailsShareHolder
    shares_count: int
    shares_percentage: float

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
            shares_count=row['shares_count'],
            shares_percentage=row['shares_percentage'],
        ) for row in raw_data]

    class Config:
        arbitrary_types_allowed = True
