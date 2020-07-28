import json
import math
import re

import requests
from bs4 import BeautifulSoup

_script_vars_pattern = re.compile("var (?P<name>.*)=(?P<content>\[[^;]*\]);")


def _load_script_vars(asset_id, year, month, day):
    d = f'{year:04}{month:02}{day:02}'
    script_variables = {}

    # get data from url
    daily_content = requests.get(f'http://cdn.tsetmc.com/Loader.aspx?ParTree=15131P&i={asset_id}&d={d}', timeout=5).text

    # find and get script tags
    all_scripts = BeautifulSoup(daily_content, 'lxml').find_all('script')
    first_script = str(all_scripts[-3])
    second_script = str(all_scripts[-2])
    third_script = str(all_scripts[-1])

    # extract first script variables
    matches = _script_vars_pattern.findall(first_script)
    for match in matches:
        script_variables[match[0]] = json.loads(match[1].replace('\'', '"'))

    # extract second script variables
    matches = _script_vars_pattern.findall(second_script)
    for match in matches:
        script_variables[match[0]] = json.loads(match[1].replace('\'', '"'))

    # extract third script variables
    matches = _script_vars_pattern.findall(third_script)
    for match in matches:
        script_variables[match[0]] = json.loads(match[1].replace('\'', '"'))

    return script_variables


def _extract_asset_details_data(script_vars):
    asset_details = {
        'full_name': script_vars['InstSimpleData'][0],
        'short_name': script_vars['InstSimpleData'][1],
        'market_short_name': script_vars['InstSimpleData'][2],
        'market_full_name': script_vars['InstSimpleData'][3],
        'isin': script_vars['InstSimpleData'][7],
        'shares_count': script_vars['InstSimpleData'][8],
        'base_volume': script_vars['InstSimpleData'][9],
    }

    return asset_details


def _extract_price_data(script_vars):
    # State Data
    state_data = []
    for isd in script_vars['InstrumentStateData']:
        state_data.append(isd[1:])

    last_state_i = 0
    next_state_change_time = state_data[0][0] if len(state_data) > 1 else math.inf
    last_state = state_data[0][1] if len(state_data) > 1 else 'A '  # todo: convert to enum

    # Price Data
    price_data = []
    for cpd in script_vars['ClosingPriceData']:
        continuous_time = int(cpd[12])
        while continuous_time >= next_state_change_time:
            if len(state_data) > (last_state_i + 1):
                last_state_i += 1
                next_state_change_time = state_data[last_state_i][0]
                last_state = state_data[last_state_i][1]  # todo: convert to enum
            else:
                next_state_change_time = math.inf

        price_data.append({
            'time': continuous_time,
            'last': int(cpd[2]),
            'yesterday': int(cpd[5]),
            'open': int(cpd[4]),
            'close': int(cpd[3]),
            'high': int(cpd[6]),
            'low': int(cpd[7]),
            'count': int(cpd[8]),
            'volume': int(cpd[9]),
            'state': last_state,
        })

    price_data.sort(key=lambda x: x['t'])
    return price_data


def _extract_orders_data(script_vars):
    orders = []
    for bld in script_vars['BestLimitData']:
        order = {
            'time': bld[0],
            'order': int(bld[1]),
            'buy_count': int(bld[2]),
            'buy_volume': int(bld[3]),
            'buy_price': int(bld[4]),
            'sell_count': int(bld[7]),
            'sell_volume': int(bld[6]),
            'sell_price': int(bld[5]),
        }

        orders.append(order)

    orders.sort(key=lambda x: x['t'])
    return orders


def _extract_trade_data(script_vars):
    trades = [
        {
            'order': int(x[0]),
            'time': int(f'{x[1][:2]}{x[1][3:5]}{x[1][6:]}'),
            'volume': int(x[2]),
            'price': int(x[3]),
        }
        for x in script_vars['IntraTradeData']
    ]

    return trades


def _extract_shareholders_data(script_vars):
    shareholders = []
    for shd in script_vars['ShareHolderData']:
        shareholders.append({
            'id': shd[0],
            'shares_count': shd[2],
            'shares_percent': shd[3],
            'name': shd[5],
        })

    yesterday_shareholders = []
    for shd in script_vars['ShareHolderDataYesterday']:
        yesterday_shareholders.append({
            'id': shd[0],
            'shares_count': shd[2],
            'shares_percent': shd[3],
            'name': shd[5],
        })

    return yesterday_shareholders, shareholders


def load_intraday_history_data(asset_id, year, month, day):
    """
    اطلاعات نماد در یک روز خاص (نماد >‌ سابقه > دبل کلیک روی یک روز خاص)
    """

    script_vars = _load_script_vars(asset_id, year, month, day)

    ret = {}

    ret['asset_details'] = _extract_asset_details_data(script_vars)
    ret['price_data'] = _extract_price_data(script_vars)

    if not ret['price_data']:
        return None

    ret['orders'] = _extract_orders_data(script_vars)
    ret['trades'] = _extract_trade_data(script_vars)
    ret['shareholders_yesterday'], ret['shareholders_today'] = _extract_shareholders_data(script_vars)

    return ret
