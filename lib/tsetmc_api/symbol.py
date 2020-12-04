from typing import List

from jdatetime import date as jdate

from .core import shareholder as shareholder_core
from .core import symbol as symbol_core
from tsetmc_api.cache import MemoryCache
from .day_details import SymbolDayDetails
from .shareholder import SymbolMajorShareholder


class Symbol:
    def __init__(self, symbol_id):
        self.id = symbol_id

    def get_price_data(self):
        """
        اطلاعات قیمت لحظه‌ای
        """
        # todo
        raise NotImplementedError('sorry, price date of symbol has not been implemented yet :(')

    def get_details(self) -> dict:
        """
        شناسه
        """
        if MemoryCache.exists('symbol_details', self.id):
            return MemoryCache.fetch('symbol_details', self.id)

        raw_details = symbol_core.get_symbol_details(self.id)
        ret = {
            'isin': raw_details.get('کد 12 رقمی نماد', None),
            'short_isin': raw_details.get('کد 5 رقمی نماد', None),
            'short_name': raw_details.get('نماد فارسی', None),
            'long_name': raw_details.get('نماد 30 رقمی فارسی', None),
            'english_name': raw_details.get('نام لاتین شرکت', None),

            'company_isin': raw_details.get('کد 12 رقمی شرکت', None),
            'company_short_isin': raw_details.get('کد 4 رقمی شرکت', None),
            'company_name': raw_details.get('نام شرکت', None),

            'market_code': raw_details.get('کد تابلو', None),
            'market_name': raw_details.get('بازار', None),

            'group_code': raw_details.get('کد گروه صنعت', None),
            'group_name': raw_details.get('گروه صنعت', None),

            'subgroup_code': raw_details.get('کد زیر گروه صنعت', None),
            'subgroup_name': raw_details.get('زیر گروه صنعت', None),
        }

        for key in ret:
            if isinstance(ret[key], str):
                ret[key] = ret[key].strip()

        MemoryCache.store('symbol_details', self.id, ret)

        return ret

    def get_daily_history(self) -> List[dict]:
        """
        سابقه
        """
        if MemoryCache.exists('symbol_daily_history', self.id):
            return MemoryCache.fetch('symbol_daily_history', self.id)

        raw_history = symbol_core.get_daily_history(self.id)
        ret = []

        for raw_day in raw_history:
            ret.append({
                'date': jdate.fromgregorian(date=raw_day['date']),
                'count': raw_day['count'],
                'volume': raw_day['volume'],
                'value': raw_day['value'],
                'yesterday': raw_day['yesterday_price'],
                'last': raw_day['last_price'],
                'first': raw_day['first_price'],
                'close': raw_day['close_price'],
                'low': raw_day['low_price'],
                'high': raw_day['high_price'],
            })

        MemoryCache.store('symbol_daily_history', self.id, ret)

        return ret

    def get_day_details(self, jyear: int, jmonth: int, jday: int) -> SymbolDayDetails:
        """
        اطلاعات یک روز خاص در سابقه
        """
        return SymbolDayDetails(self, jyear, jmonth, jday)

    def get_client_type_history(self) -> List[dict]:
        """
        تاریخچه‌ی حقیقی حقوقی
        """
        if MemoryCache.exists('symbol_client_type_history', self.id):
            return MemoryCache.fetch('symbol_client_type_history', self.id)

        raw_history = shareholder_core.get_client_type_history(self.id)
        ret = []
        for raw_proportion in raw_history:
            t = raw_proportion[0]
            ret.append({
                'date': jdate.fromgregorian(year=int(t[:4]), month=int(t[4:6]), day=int(t[6:])),
                'natural': {
                    'buy_count': int(raw_proportion[1]),
                    'buy_volume': int(raw_proportion[5]),
                    'buy_value': int(raw_proportion[9]),
                    'sell_count': int(raw_proportion[3]),
                    'sell_volume': int(raw_proportion[7]),
                    'sell_value': int(raw_proportion[11]),
                },
                'legal': {
                    'buy_count': int(raw_proportion[2]),
                    'buy_volume': int(raw_proportion[6]),
                    'buy_value': int(raw_proportion[10]),
                    'sell_count': int(raw_proportion[4]),
                    'sell_volume': int(raw_proportion[8]),
                    'sell_value': int(raw_proportion[12]),
                },
            })

        MemoryCache.store('symbol_client_type_history', self.id, ret)

        return ret

    def get_major_shareholders(self) -> List[SymbolMajorShareholder]:
        """
        لیست سهامداران عمده
        """
        if MemoryCache.exists('symbol_major_shareholders', self.id):
            return MemoryCache.fetch('symbol_major_shareholders', self.id)

        company_isin = self.get_details()['company_isin']
        raw_majors = shareholder_core.get_major_shareholders(company_isin)
        ret = []
        for raw_major in raw_majors:
            ret.append(
                SymbolMajorShareholder(self.id,
                                       company_isin=company_isin,
                                       holder_name=raw_major['name'],
                                       holder_id=raw_major['id'],
                                       percentage=raw_major['percentage'],
                                       shares_count=raw_major['shares_count'],
                                       change=raw_major['change'])
            )

        MemoryCache.store('symbol_major_shareholders', self.id, ret)

        return ret

    def __str__(self):
        return f'Symbol > {self.id}'
