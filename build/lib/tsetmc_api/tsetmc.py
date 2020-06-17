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


def get_daily_history(symbol_i, offset=999999):
    ret = []

    daily_content = requests.get(
        f'http://members.tsetmc.com/tsev2/data/InstTradeHistory.aspx?i={symbol_i}&Top={offset}&A=0').text

    raw_ticks = daily_content.split(';')

    for raw_tick in raw_ticks:
        if raw_tick == '':
            continue

        tick_data = raw_tick.split('@')

        time = tick_data[0]
        high_price = tick_data[1]
        low_price = tick_data[2]
        end_price = tick_data[3]
        last_price = tick_data[4]
        open_price = tick_data[5]
        yesterday_price = tick_data[6]
        value = tick_data[7]
        volume = tick_data[8]

        ret.append({
            't': time,
            'h': int(high_price[:-3]),
            'l': int(low_price[:-3]),
            'c': int(end_price[:-3]),
            'p': int(last_price[:-3]),
            'o': int(open_price[:-3]),
            'y': int(yesterday_price[:-3]),
            'value': int(float(value)),
            'v': int(float(volume)),
        })

    return ret
