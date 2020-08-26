from jdatetime import date as jdate

from .core import asset as asset_core
from .core import shareholder as shareholder_core
from .core.cache import MemoryCache
from .day_details import AssetDayDetails
from .shareholder import AssetMajorShareholder


class Asset:
    def __init__(self, asset_id):
        self.id = asset_id

    def get_price_data(self):
        """
        اطلاعات قیمت لحظه‌ای
        """
        # todo
        raise NotImplementedError('sorry, price date of asset has not been implemented yet :(')

    def get_details(self):
        """
        شناسه
        """
        if MemoryCache.exists('asset_details', self.id):
            return MemoryCache.fetch('asset_details', self.id)

        raw_details = asset_core.get_asset_details(self.id)
        ret = {
            'symbol_isin': raw_details.get('کد 12 رقمی نماد', None),
            'symbol_short_isin': raw_details.get('کد 5 رقمی نماد', None),
            'symbol_short_name': raw_details.get('نماد فارسی', None),
            'symbol_long_name': raw_details.get('نماد 30 رقمی فارسی', None),
            'symbol_english_name': raw_details.get('نام لاتین شرکت', None),

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

        MemoryCache.store('asset_details', self.id, ret)

        return ret

    def get_daily_history(self):
        """
        سابقه
        """
        if MemoryCache.exists('asset_daily_history', self.id):
            return MemoryCache.fetch('asset_daily_history', self.id)

        raw_history = asset_core.get_daily_history(self.id)
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

        MemoryCache.store('asset_daily_history', self.id, ret)

        return ret

    def get_day_details(self, jyear, jmonth, jday):
        """
        اطلاعات یک روز خاص در سابقه
        """
        return AssetDayDetails(self, jyear, jmonth, jday)

    def get_client_type_history(self):
        """
        تاریخچه‌ی حقیقی حقوقی
        """
        if MemoryCache.exists('asset_client_type_history', self.id):
            return MemoryCache.fetch('asset_client_type_history', self.id)

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

        MemoryCache.store('asset_client_type_history', self.id, ret)

        return ret

    def get_major_shareholders(self):
        """
        لیست سهامداران عمده
        """
        if MemoryCache.exists('asset_major_shareholders', self.id):
            return MemoryCache.fetch('asset_major_shareholders', self.id)

        company_isin = self.get_details()['company_isin']
        raw_majors = shareholder_core.get_major_shareholders(company_isin)
        ret = []
        for raw_major in raw_majors:
            ret.append(
                AssetMajorShareholder(self.id,
                                      company_isin=company_isin,
                                      holder_name=raw_major['name'],
                                      holder_id=raw_major['id'],
                                      percentage=raw_major['percentage'],
                                      shares_count=raw_major['shares_count'],
                                      change=raw_major['change'])
            )

        MemoryCache.store('asset_major_shareholders', self.id, ret)

        return ret

    def __str__(self):
        return f'Asset > {self.id}'
