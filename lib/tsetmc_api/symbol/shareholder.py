from typing import Any

from jdatetime import date as jdate
from pydantic import BaseModel, PrivateAttr

from . import _core
from ..utils import run_sync_function


class SymbolShareHolderPortfolioRow(BaseModel):
    symbol_id: str
    long_name: str
    shares_count: int
    shares_percentage: float


class SymbolShareHolder(BaseModel):
    _company_isin: str = PrivateAttr()
    id: str
    name: str

    def __init__(self, _company_isin: str, **data: Any):
        super().__init__(**data)
        self._company_isin = _company_isin

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
            shares_count=row['shares_count'],
            shares_percentage=row['shares_percentage'],
        ) for row in raw_data]

    async def get_portfolio_data_async(self) -> list[SymbolShareHolderPortfolioRow]:
        """
        returns list of companies owned by this shareholder
        """

        return await run_sync_function(
            func=self.get_portfolio_data,
        )


class SymbolShareHolderChartRow(BaseModel):
    date: jdate
    shares_count: int

    class Config:
        arbitrary_types_allowed = True


class SymbolShareHolderDataRow(BaseModel):
    shareholder: SymbolShareHolder
    shares_count: int
    shares_percentage: float
    shares_change: int

    def get_chart_data(self) -> list[SymbolShareHolderChartRow]:
        """
        returns list of changes to shareholders share count in history of this symbol
        """

        raw_data = _core.get_symbol_shareholder_details(
            shareholder_id=self.shareholder.id,
            company_isin=self.shareholder._company_isin,
        )['chart']

        return [SymbolShareHolderChartRow(
            date=row['date'],
            shares_count=row['shares_count'],
        ) for row in raw_data]

    async def get_chart_data_async(self) -> list[SymbolShareHolderChartRow]:
        """
        returns list of changes to shareholders share count in history of this symbol
        """

        return await run_sync_function(
            func=self.get_chart_data,
        )
