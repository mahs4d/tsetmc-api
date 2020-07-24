import json
from os import path

import pkg_resources
import requests

from .day_details import AssetDayDetails


# region daily history

def _load_raw_daily_history(asset_id, limit):
    daily_content = requests.get(
        f'http://members.tsetmc.com/tsev2/data/InstTradeHistory.aspx?i={asset_id}&Top={limit}&A=0',
        timeout=5).text
    print('loaded')
    raw_ticks = daily_content.split(';')

    return raw_ticks


def _extract_daily_history(raw_ticks):
    ticks = []
    for raw_tick in raw_ticks:
        if raw_tick == '':
            continue

        tick_data = raw_tick.split('@')

        time = tick_data[0]
        high_price = tick_data[1]
        low_price = tick_data[2]
        close_price = tick_data[3]
        last_price = tick_data[4]
        first_price = tick_data[5]
        yesterday_price = tick_data[6]
        value = tick_data[7]
        volume = tick_data[8]

        ticks.append({
            'time': time,  # todo: parse
            'first_price': int(first_price[:-3]),
            'high_price': int(high_price[:-3]),
            'low_price': int(low_price[:-3]),
            'close_price': int(close_price[:-3]),
            'last_price': int(last_price[:-3]),
            'yesterday_price': int(yesterday_price[:-3]),
            'value': int(float(value)),
            'volume': int(float(volume)),
        })

    return ticks


# endregion

# region client type

def _load_raw_client_type_data(asset_id):
    client_types_raw = requests.get(f'http://www.tsetmc.com/tsev2/data/clienttype.aspx?i={asset_id}', timeout=5).text
    client_types_raw = client_types_raw.split(';')

    return client_types_raw


def _extract_client_type_history(raw_client_type_data):
    ret = []
    for client_type_day in raw_client_type_data:
        if client_type_day == '':
            continue

        tick_data = client_type_day.split(',')

        time = tick_data[0]
        individual_buy_count = tick_data[1]
        corporate_buy_count = tick_data[2]
        individual_sell_count = tick_data[3]
        corporate_sell_count = tick_data[4]
        individual_buy_vol = tick_data[5]
        corporate_buy_vol = tick_data[6]
        individual_sell_vol = tick_data[7]
        corporate_sell_vol = tick_data[8]
        individual_buy_value = tick_data[9]
        corporate_buy_value = tick_data[10]
        individual_sell_value = tick_data[11]
        corporate_sell_value = tick_data[12]

        ret.append({
            'time': time,  # todo: parse
            'individual_buy_count': int(individual_buy_count),
            'corporate_buy_count': int(corporate_buy_count),
            'individual_sell_count': int(individual_sell_count),
            'corporate_sell_count': int(corporate_sell_count),
            'individual_buy_vol': int(individual_buy_vol),
            'corporate_buy_vol': int(corporate_buy_vol),
            'individual_sell_vol': int(individual_sell_vol),
            'corporate_sell_vol': int(corporate_sell_vol),
            'individual_buy_value': int(individual_buy_value),
            'corporate_buy_value': int(corporate_buy_value),
            'individual_sell_value': int(individual_sell_value),
            'corporate_sell_value': int(corporate_sell_value),
        })

    return ret


# endregion

# region search assets

def _find_asset(q):
    search_raw = requests.get(f'http://www.tsetmc.com/tsev2/data/search.aspx?skey={q}', timeout=5).text.split(';')

    if not search_raw or search_raw[0] == '':
        return None

    first_result = search_raw[0].split(',')
    return {
        'id': first_result[2],
        'full_name': first_result[1],
        'short_name': first_result[0],
    }


# endregion

class Asset:
    def __init__(self, asset_id, short_name=None, full_name=None, isin=None):
        self.asset_id = asset_id
        self.short_name = short_name
        self.full_name = full_name
        self.isin = isin

    def get_daily_history(self, limit=999999):
        raw_daily_history = _load_raw_daily_history(self.asset_id, limit)
        daily_history = _extract_daily_history(raw_daily_history)
        return daily_history

    def get_client_type_history(self):
        raw_client_type_data = _load_raw_client_type_data(self.asset_id)
        client_type_history = _extract_client_type_history(raw_client_type_data)
        return client_type_history

    def get_day_details(self, year, month, day, use_cache=True,
                        cache_address=path.expanduser('~/.tsetmc-api/intraday-cache')):
        return AssetDayDetails(self.asset_id, year, month, day, use_cache=use_cache, cache_address=cache_address)

    @staticmethod
    def find_asset(q):
        search_result = _find_asset(q)

        if search_result is None:
            raise Exception('not found')

        return Asset(asset_id=search_result['id'],
                     short_name=search_result['short_name'],
                     full_name=search_result['full_name'])

    @staticmethod
    def get_assets():
        """
        this list is by no means complete
        """
        json_path = pkg_resources.resource_filename('tsetmc_api', 'data/assets.json')
        with open(json_path, 'r') as fp:
            parsed = json.load(fp)
            assets = [Asset(asset_id=asset_identifier['id'],
                            short_name=asset_identifier['short_name'],
                            full_name=asset_identifier['full_name']) for asset_identifier in parsed]

        return assets
