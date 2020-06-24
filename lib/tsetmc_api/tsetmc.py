import json
import re

import requests
from bs4 import BeautifulSoup

intraday_pattern = re.compile("var (?P<name>.*)=(?P<content>\[[^;]*\]);")


def get_intraday_history(i, d):
    vars = {}

    daily_content = requests.get('http://cdn.tsetmc.com/Loader.aspx?ParTree=15131P&i={}&d={}'.format(i, d)).text

    all_scripts = BeautifulSoup(daily_content).find_all('script')

    first_script = str(all_scripts[-3])
    second_script = str(all_scripts[-2])
    third_script = str(all_scripts[-1])

    # first script
    matches = intraday_pattern.search(first_script)
    vars[matches.group('name')] = matches.group('content')

    # second script
    matches = intraday_pattern.findall(second_script)
    for match in matches:
        vars[match[0]] = json.loads(match[1].replace('\'', '"'))

    # third script
    matches = intraday_pattern.search(third_script)
    vars[matches.group('name')] = matches.group('content')

    return vars


def get_daily_history(asset_id, limit=999999):
    ret = []

    daily_content = requests.get(
        f'http://members.tsetmc.com/tsev2/data/InstTradeHistory.aspx?i={asset_id}&Top={limit}&A=0').text

    raw_ticks = daily_content.split(';')

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

        ret.append({
            'time': time,
            'first_price': int(first_price[:-3]),
            'high_price': int(high_price[:-3]),
            'low_price': int(low_price[:-3]),
            'close_price': int(close_price[:-3]),
            'last_price': int(last_price[:-3]),
            'yesterday_price': int(yesterday_price[:-3]),
            'value': int(float(value)),
            'volume': int(float(volume)),
        })

    return ret


def get_client_type_history(asset_id):
    ret = []

    client_types_raw = requests.get(f'http://www.tsetmc.com/tsev2/data/clienttype.aspx?i={asset_id}').text
    client_types_raw = client_types_raw.split(';')

    for client_type_day in client_types_raw:
        if client_type_day == '':
            continue

        tick_data = client_type_day.split(',')

        time = tick_data[0]
        haghighi_buy_count = tick_data[1]
        hoghooghi_buy_count = tick_data[2]
        haghighi_sell_count = tick_data[3]
        hoghooghi_sell_count = tick_data[4]
        haghighi_buy_vol = tick_data[5]
        hoghooghi_buy_vol = tick_data[6]
        haghighi_sell_vol = tick_data[7]
        hoghooghi_sell_vol = tick_data[8]
        haghighi_buy_value = tick_data[9]
        hoghooghi_buy_value = tick_data[10]
        haghighi_sell_value = tick_data[11]
        hoghooghi_sell_value = tick_data[12]

        ret.append({
            'time': time,
            'haghighi_buy_count': int(haghighi_buy_count),
            'hoghooghi_buy_count': int(hoghooghi_buy_count),
            'haghighi_sell_count': int(haghighi_sell_count),
            'hoghooghi_sell_count': int(hoghooghi_sell_count),
            'haghighi_buy_vol': int(haghighi_buy_vol),
            'hoghooghi_buy_vol': int(hoghooghi_buy_vol),
            'haghighi_sell_vol': int(haghighi_sell_vol),
            'hoghooghi_sell_vol': int(hoghooghi_sell_vol),
            'haghighi_buy_value': int(haghighi_buy_value),
            'hoghooghi_buy_value': int(hoghooghi_buy_value),
            'haghighi_sell_value': int(haghighi_sell_value),
            'hoghooghi_sell_value': int(hoghooghi_sell_value),
        })

    return ret
