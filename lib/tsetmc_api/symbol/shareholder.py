from jdatetime import date as jdate
from pydantic import BaseModel

from . import _core


class SymbolShareHolderPortfolioRow(BaseModel):
    symbol_id: str
    long_name: str
    count: int
    percentage: float


class SymbolShareHolder(BaseModel):
    _company_isin: str
    id: str
    name: str

    def get_portfolio_data(self) -> list[SymbolShareHolderPortfolioRow]:
        """
        returns list of companies owned by this shareholder
        """

        raw_data = _core.get_symbol_shareholder_details(
            shareholder_id=self.id,
            company_isin=self._company_isin,
        )['portfolio']

        return [SymbolShareHolderPortfolioRow(
            symbol_id=row['symbol_id'],
            long_name=row['long_name'],
            count=row['count'],
            percentage=row['percentage'],
        ) for row in raw_data]


class SymbolShareHolderChartRow(BaseModel):
    date: jdate
    count: int

    class Config:
        arbitrary_types_allowed = True


class SymbolShareHolderDataRow(BaseModel):
    shareholder: SymbolShareHolder
    count: int
    percentage: float
    change: int

    def get_chart_data(self) -> list[SymbolShareHolderChartRow]:
        """
        returns list of changes to shareholders share count in history of this symbol
        """

        raw_data = _core.get_symbol_shareholder_details(
            shareholder_id=self.shareholder.id,
            company_isin=self.shareholder._company_isin,
        )

        return [SymbolShareHolderChartRow(
            date=row['date'],
            count=row['count'],
        ) for row in raw_data]
