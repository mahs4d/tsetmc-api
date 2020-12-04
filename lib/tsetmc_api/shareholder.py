from typing import List

from jdatetime import date as jdate

from .core import shareholder as shareholder_core
from tsetmc_api.cache import MemoryCache


class SymbolMajorShareholder:
    def __init__(self, symbol_id: str, company_isin: str, holder_name: str, holder_id: str, percentage: float,
                 shares_count: int, change: int = None):
        self.symbol_id = symbol_id
        self.company_isin = company_isin
        self.name = holder_name
        self.id = holder_id
        self.percentage = percentage
        self.shares_count = shares_count
        self.change = change

    def _get_details(self) -> dict:
        if MemoryCache.exists('major_shareholder_details', self.id):
            return MemoryCache.fetch('major_shareholder_details', self.id)
        raw = shareholder_core.get_major_shareholder_details(self.company_isin, self.id)

        ret = {
            'activities': [],
            'other_symbols': [],
        }
        for activity in raw['activities']:
            ret['activities'].append({
                'date': jdate.fromgregorian(date=activity['date']),
                'shares_count': activity['shares_count'],
            })

        from .symbol import Symbol
        for raw_symbol in raw['other_symbols']:
            ret['other_symbols'].append({
                'symbol': Symbol(raw_symbol['symbol_id']),
                'company_name': raw_symbol['company_name'],
                'shares_count': raw_symbol['shares_count'],
                'percentage': raw_symbol['percentage'],
            })

        MemoryCache.store('major_shareholder_details', self.id, ret)
        return ret

    def get_activity_history(self) -> List[dict]:
        """
        گرفتن سابقه‌ی فرد در این سهم (نمودار سهامدار عمده)
        """
        return self._get_details()['activities']

    def get_other_major_symbols(self) -> List[dict]:
        """
        سهم‌های دیگری که این فرد در آن‌ها هم سهامدار عمده است
        """
        return self._get_details()['other_symbols']

    def __str__(self):
        return f'SymbolMajorShareholder > {self.symbol_id}/{self.id} - {self.name}'
