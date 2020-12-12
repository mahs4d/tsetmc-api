import json
import math
import re

import requests
from bs4 import BeautifulSoup

from .exceptions import NoDataError

_intraday_pattern = re.compile("var (?P<name>.*)=(?P<content>\[[^;]*\]);")


def _load_script_vars_from_web(symbol_id, year, month, day):
    d = f'{year:04}{month:02}{day:02}'
    script_variables = {}

    # get data from url
    daily_content = requests.get(f'http://cdn.tsetmc.com/Loader.aspx?ParTree=15131P&i={symbol_id}&d={d}',
                                 timeout=20, verify=False).text

    # find and get script tags
    all_scripts = BeautifulSoup(daily_content, 'lxml').find_all('script')
    first_script = str(all_scripts[-3])
    second_script = str(all_scripts[-2])
    third_script = str(all_scripts[-1])

    # extract first script variables
    matches = _intraday_pattern.findall(first_script)
    for match in matches:
        script_variables[match[0]] = json.loads(match[1].replace('\'', '"'))

    # extract second script variables
    matches = _intraday_pattern.findall(second_script)
    for match in matches:
        script_variables[match[0]] = json.loads(match[1].replace('\'', '"'))

    # extract third script variables
    matches = _intraday_pattern.findall(third_script)
    for match in matches:
        script_variables[match[0]] = json.loads(match[1].replace('\'', '"'))

    return script_variables


def _extract_symbol_details_data(script_vars):
    symbol_details = {
        'full_name': script_vars['InstSimpleData'][0],
        'short_name': script_vars['InstSimpleData'][1],
        'market_short_name': script_vars['InstSimpleData'][2],
        'market_full_name': script_vars['InstSimpleData'][3],
        'isin': script_vars['InstSimpleData'][7],
        'shares_count': script_vars['InstSimpleData'][8],
        'base_volume': script_vars['InstSimpleData'][9],
    }

    return symbol_details


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
            't': continuous_time,
            'lst': int(cpd[2]),
            'y': int(cpd[5]),
            'o': int(cpd[4]),
            'c': int(cpd[3]),
            'h': int(cpd[6]),
            'l': int(cpd[7]),
            'cnt': int(cpd[8]),
            'v': int(cpd[9]),
            's': last_state,
        })

    price_data.sort(key=lambda x: x['t'])
    return price_data


def _extract_orders_data(script_vars):
    orders = []
    for bld in script_vars['BestLimitData']:
        order = {
            't': bld[0],
            'rank': int(bld[1]),
            'bcnt': int(bld[2]),
            'bv': int(bld[3]),
            'bp': int(bld[4]),
            'scnt': int(bld[7]),
            'sv': int(bld[6]),
            'sp': int(bld[5]),
        }

        orders.append(order)

    orders.sort(key=lambda x: x['t'])
    return orders


def _extract_trade_data(script_vars):
    trades = [
        {
            'order': int(x[0]),
            't': int(f'{x[1][:2]}{x[1][3:5]}{x[1][6:]}'),
            'v': int(x[2]),
            'p': int(x[3]),
        }
        for x in script_vars['IntraTradeData']
    ]

    return trades


def _extract_share_holders_data(script_vars):
    share_holders = []
    for shd in script_vars['ShareHolderData']:
        share_holders.append({
            'id': shd[0],
            'shares_count': shd[2],
            'percentage': shd[3],
            'name': shd[5],
        })

    previous_share_holders = []
    for shd in script_vars['ShareHolderDataYesterday']:
        previous_share_holders.append({
            'id': shd[0],
            'shares_count': shd[2],
            'percentage': shd[3],
            'name': shd[5],
        })

    return previous_share_holders, share_holders


def load_intraday_data(symbol_id, year, month, day):
    script_vars = _load_script_vars_from_web(symbol_id, year, month, day)

    symbol_details = _extract_symbol_details_data(script_vars)
    price_data = _extract_price_data(script_vars)

    if not price_data:
        raise NoDataError('there is no data for this symbol in the specified date')

    previous_shareholders, shareholders = _extract_share_holders_data(script_vars)
    trades = _extract_trade_data(script_vars)
    orders_data = _extract_orders_data(script_vars)

    return {
        'symbol_details': symbol_details,
        'price_data': price_data,
        'previous_shareholders': previous_shareholders,
        'shareholders': shareholders,
        'trades': trades,
        'orders_data': orders_data,
    }
