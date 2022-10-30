from collections import defaultdict
from copy import deepcopy

import requests
from jdatetime import date as jdate

from ..utils import convert_deven_to_jdate, convert_heven_to_jtime


def get_day_details_price_overview(symbol_id: str, date: jdate) -> dict:
    t = date.togregorian().strftime('%Y%m%d')
    response = requests.get(
        url=f'http://cdn.tsetmc.com/api/ClosingPrice/GetClosingPriceDaily/{symbol_id}/{t}',
        params={},
        verify=False,
        timeout=20,
    )
    response.raise_for_status()
    response = response.json()['closingPriceDaily']

    return {
        "price_change": response["priceChange"],
        "low": response["priceMin"],
        "high": response["priceMax"],
        "yesterday": response["priceYesterday"],
        "open": response["priceFirst"],
        "close": response["pClosing"],
        "last": response["pDrCotVal"],
        "count": response["zTotTran"],
        "volume": response["qTotTran5J"],
        "value": response["qTotCap"],
    }


def get_day_details_price_data(symbol_id: str, date: jdate) -> list[dict]:
    t = date.togregorian().strftime('%Y%m%d')
    response = requests.get(
        url=f'http://cdn.tsetmc.com/api/ClosingPrice/GetClosingPriceHistory/{symbol_id}/{t}',
        params={},
        verify=False,
        timeout=20,
    )
    response.raise_for_status()
    response = response.json()['closingPriceHistory']

    price_data = [{
        'time': convert_heven_to_jtime(heven=row['hEven']),
        'close': int(row['pClosing']),
        'last': int(row['pDrCotVal']),
        'value': int(row['qTotCap']),
        'volume': int(row['qTotTran5J']),
        'count': int(row['zTotTran']),
    } for row in response]

    return price_data


def get_day_details_orderbook_data(symbol_id: str, date: jdate) -> list[dict]:
    t = date.togregorian().strftime('%Y%m%d')
    response = requests.get(
        url=f'http://cdn.tsetmc.com/api/BestLimits/{symbol_id}/{t}',
        params={},
        verify=False,
        timeout=20,
    )
    response.raise_for_status()
    response = response.json()['bestLimitsHistory']
    response = sorted(response, key=lambda x: (x['hEven'], x['number']))

    prev_data = {'buy_rows': [], 'sell_rows': []}
    heven_map = defaultdict(lambda: {'buy_rows': [], 'sell_rows': []})
    for row in response:
        heven = row['hEven']
        t = convert_heven_to_jtime(heven=heven)

        buy_row = {
            'time': t,
            'count': row['zOrdMeDem'],
            'price': row['pMeDem'],
            'volume': row['qTitMeDem'],
        }
        sell_row = {
            'time': t,
            'count': row['zOrdMeOf'],
            'price': row['pMeOf'],
            'volume': row['qTitMeOf'],
        }

        index = row['number'] - 1

        if heven not in heven_map:
            heven_map[heven] = deepcopy(prev_data)

        while len(heven_map[heven]['buy_rows']) < index + 1:
            heven_map[heven]['buy_rows'].append(None)

        while len(heven_map[heven]['sell_rows']) < index + 1:
            heven_map[heven]['sell_rows'].append(None)

        heven_map[heven]['buy_rows'][index] = buy_row
        heven_map[heven]['sell_rows'][index] = sell_row

        prev_data = heven_map[heven]

    return [{
        'time': convert_heven_to_jtime(heven=key),
        **value,
    } for key, value in heven_map.items()]


def get_day_details_trade_data(symbol_id: str, date: jdate, summarize: bool) -> list[dict]:
    t = date.togregorian().strftime('%Y%m%d')
    summarize_url_ph = 'true' if summarize else 'false'
    response = requests.get(
        url=f'http://cdn.tsetmc.com/api/Trade/GetTradeHistory/{symbol_id}/{t}/{summarize_url_ph}',
        params={},
        verify=False,
        timeout=20,
    )
    response.raise_for_status()
    response = response.json()['tradeHistory']

    return [{
        'time': convert_heven_to_jtime(heven=row['hEven']),
        'price': row['pTran'],
        'volume': row['qTitTran'],
    } for row in response]


def get_day_details_traders_type_data(symbol_id: str, date: jdate) -> dict:
    t = date.togregorian().strftime('%Y%m%d')
    response = requests.get(
        url=f'http://cdn.tsetmc.com/api/ClientType/GetClientTypeHistory/{symbol_id}/{t}',
        params={},
        verify=False,
        timeout=20,
    )
    response.raise_for_status()
    response = response.json()['clientType']

    return {
        'legal': {
            'buy': {
                'volume': response['buy_N_Volume'],
                'value': response['buy_N_Value'],
                'count': response['buy_N_Count'],
            },
            'sell': {
                'volume': response['sell_N_Volume'],
                'value': response['sell_N_Value'],
                'count': response['sell_N_Count'],
            }
        },
        'real': {
            'buy': {
                'volume': response['buy_I_Volume'],
                'value': response['buy_I_Value'],
                'count': response['buy_I_Count'],
            },
            'sell': {
                'volume': response['sell_I_Volume'],
                'value': response['sell_I_Value'],
                'count': response['sell_I_Count'],
            }
        },
    }


def get_day_details_thresholds_data(symbol_id: str, date: jdate) -> dict:
    t = date.togregorian().strftime('%Y%m%d')
    response = requests.get(
        url=f'http://cdn.tsetmc.com/api/MarketData/GetStaticThreshold/{symbol_id}/{t}',
        params={},
        verify=False,
        timeout=20,
    )
    response.raise_for_status()
    response = response.json()['staticThreshold']

    return {
        'max': response[1]['psGelStaMax'],
        'min': response[1]['psGelStaMin'],
    }


def get_day_details_shareholders_data(symbol_id: str, date: jdate) -> tuple[list[dict], list[dict]]:
    t = date.togregorian().strftime('%Y%m%d')
    response = requests.get(
        url=f'http://cdn.tsetmc.com/api/Shareholder/{symbol_id}/{t}',
        params={},
        verify=False,
        timeout=20,
    )
    response.raise_for_status()
    response = response.json()['shareShareholder']

    old_shareholders = []
    new_shareholders = []
    it = int(t)
    for row in response:
        sh_data = {
            'id': str(row['shareHolderId']),
            'name': row['shareHolderName'],
            'count': row['numberOfShares'],
            'percentage': row['perOfShares'],
        }

        if row['dEven'] < it:
            old_shareholders.append(sh_data)
        else:
            new_shareholders.append(sh_data)

    return old_shareholders, new_shareholders


def get_shareholder_chart_data(symbol_id: str, shareholder_id: str, days: int) -> list[dict]:
    response = requests.get(
        url=f'http://cdn.tsetmc.com/api/Shareholder/GetShareHolderHistory/{symbol_id}/{shareholder_id}/{days}',
        params={},
        verify=False,
        timeout=20,
    )
    response.raise_for_status()
    response = response.json()['shareHolder']

    return [{
        'date': convert_deven_to_jdate(deven=row['dEven']),
        'count': row['numberOfShares'],
        'percentage': row['perOfShares'],
    } for row in response]


def get_shareholder_portfolio(shareholder_id: str) -> list[dict]:
    response = requests.get(
        url=f'http://cdn.tsetmc.com/api/Shareholder/GetShareHolderCompanyList/{shareholder_id}',
        params={},
        verify=False,
        timeout=20,
    )
    response.raise_for_status()
    response = response.json()['shareHolderShare']

    return [{
        'symbol_id': row['insCodes'],
        'short_name': row['lVal18AFC'],
        'long_name': row['lVal30'],
    } for row in response]
