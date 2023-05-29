from typing import Any

from jdatetime import date as jdate
from pydantic import BaseModel, PrivateAttr

from . import _core


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

    def get_portfolio_data(self, raw_data: dict = None) -> list[SymbolShareHolderPortfolioRow]:
        """
        returns list of companies owned by this shareholder
        """
        if raw_data is None:
            raw_data = _core.get_symbol_shareholder_details(
                shareholder_id=self.id,
                company_isin=self._company_isin,
            )
        raw_data = raw_data['portfolio']
        
        return [SymbolShareHolderPortfolioRow(
            symbol_id=row['symbol_id'],
            long_name=row['long_name'],
            shares_count=row['shares_count'],
            shares_percentage=row['shares_percentage'],
        ) for row in raw_data]
    
    async def aio_get_portfolio_data(self) -> list[SymbolShareHolderPortfolioRow]:
        return self.get_portfolio_data(
            raw_data=await _core.aio_get_symbol_shareholder_details(
                shareholder_id=self.id,
                company_isin=self._company_isin,
            )
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
    
    def get_chart_data(self, raw_data: dict = None) -> list[SymbolShareHolderChartRow]:
        """
        returns list of changes to shareholders share count in history of this symbol
        """
        
        if raw_data is None:
            raw_data = _core.get_symbol_shareholder_details(
                shareholder_id=self.shareholder.id,
                company_isin=self.shareholder._company_isin,
            )
        raw_data = raw_data['chart']
        
        return [SymbolShareHolderChartRow(
            date=row['date'],
            shares_count=row['shares_count'],
        ) for row in raw_data]
    
    async def aio_get_chart_data(self) -> list[SymbolShareHolderChartRow]:
        return self.get_chart_data(
            raw_data=await _core.aio_get_symbol_shareholder_details(
                shareholder_id=self.shareholder.id,
                company_isin=self.shareholder._company_isin,
            )
        )
