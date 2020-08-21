from jdatetime import date as jdate

from .core import shareholder as shareholder_core
from .core.cache import MemoryCache


class AssetMajorShareholder:
    def __init__(self, asset_id, company_isin, holder_name, holder_id, percentage, shares_count, change=None):
        self.asset_id = asset_id
        self.company_isin = company_isin
        self.name = holder_name
        self.id = holder_id
        self.percentage = percentage
        self.shares_count = shares_count
        self.change = change

    def _get_details(self):
        if MemoryCache.exists('major_shareholder_details', self.id):
            return MemoryCache.fetch('major_shareholder_details', self.id)
        raw = shareholder_core.get_major_shareholder_details(self.company_isin, self.id)

        ret = {
            'activities': [],
            'other_assets': [],
        }
        for activity in raw['activities']:
            ret['activities'].append({
                'date': jdate.fromgregorian(date=activity['date']),
                'shares_count': activity['shares_count'],
            })

        from .asset import Asset
        for raw_asset in raw['other_assets']:
            ret['other_assets'].append({
                'asset': Asset(raw_asset['asset_id']),
                'company_name': raw_asset['company_name'],
                'shares_count': raw_asset['shares_count'],
                'percentage': raw_asset['percentage'],
            })

        MemoryCache.store('major_shareholder_details', self.id, ret)
        return ret

    def get_activity_history(self):
        """
        گرفتن سابقه‌ی فرد در این سهم (نمودار سهامدار عمده)
        """
        return self._get_details()['activities']

    def get_other_major_assets(self):
        """
        سهم‌های دیگری که این فرد در آن‌ها هم سهامدار عمده است
        """
        return self._get_details()['other_assets']

    def __str__(self):
        return f'AssetMajorShareholder > {self.asset_id}/{self.id} - {self.name}'
