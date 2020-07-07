from .day_details import AssetDayDetails


class Asset:
    def __init__(self):
        pass

    def get_day_details(self, year, month, day):
        return AssetDayDetails(self._asset_id, year, month, day)

    @staticmethod
    def get_all_assets():
        pass
