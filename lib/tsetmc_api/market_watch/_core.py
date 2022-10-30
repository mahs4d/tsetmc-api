from collections import defaultdict

import requests

_STATS_TRADES_INDICES = {
    1: 'average_value_3_month',  # میانگین ارزش معاملات در 3 ماه گذشته
    2: 'average_value_12_month',  # میانگین ارزش معاملات در 12 ماه گذشته
    3: 'average_value_rank_3_month',  # رتبه ارزش معاملات در 3 ماه گذشته
    4: 'average_value_rank_12_month',  # رتبه ارزش معاملات در 12 ماه گذشته
    5: 'average_volume_3_month',  # میانگین حجم معاملات در 3 ماه گذشته
    6: 'average_volume_12_month',  # میانگین حجم معاملات در 12 ماه گذشته
    7: 'average_volume_rank_3_month',  # رتبه حجم معاملات در 3 ماه گذشته
    8: 'average_volume_rank_12_month',  # رتبه حجم معاملات در 12 ماه گذشته
    9: 'average_count_3_month',  # میانگین دفعات معاملات روزانه در 3 ماه گذشته
    10: 'average_count_12_month',  # میانگین دفعات معاملات روزانه در 12 ماه گذشته
    11: 'average_count_rank_3_month',  # رتبه دفعات معاملات روزانه در 3 ماه گذشته
    12: 'average_count_rank_12_month',  # رتبه دفعات معاملات روزانه در 12 ماه گذشته
    13: 'average_price_no_base_last_day',  # قیمت میانگین وزنی آخرین روز - بدون دخالت حجم مبنا
    14: 'average_price_with_base_last_day',  # قیمت میانگین وزنی آخرین روز - با دخالت حجم مبنا
    15: 'value_last_day',  # ارزش معاملات آخرین روز
    16: 'volume_last_day',  # حجم معاملات آخرین روز
    17: 'count_last_day',  # دفعات معاملات در آخرین روز
}

_STATS_NEGATIVE_DAYS_INDICES = {
    18: 'days_count_3_month',  # تعداد روزهای منفی در 3 ماه گذشته
    19: 'days_count_12_month',  # تعداد روزهای منفی در 12 ماه گذشته
    20: 'days_percent_3_month',  # درصد روزهای منفی در 3 ماه گذشته
    21: 'days_percent_12_month',  # درصد روزهای منفی در 12 ماه گذشته
    22: 'days_rank_3_month',  # رتبه روزهای منفی در 3 ماه گذشته
    23: 'days_rank_12_month',  # رتبه روزهای منفی در 12 ماه گذشته
}

_STATS_NO_TRADE_DAYS_INDICES = {
    24: 'days_count_3_month',  # روزهای بدون معامله در 3 ماه گذشته
    25: 'days_count_12_month',  # روزهای بدون معامله در 12 ماه گذشته
}

_STATS_POSITIVE_DAYS_INDICES = {
    26: 'days_count_3_month',  # تعداد روزهای مثبت در 3 ماه گذشته
    27: 'days_count_12_month',  # تعداد روزهای مثبت در 12 ماه گذشته
    28: 'days_percent_3_month',  # درصد روزهای مثبت در 3 ماه گذشته
    29: 'days_percent_12_month',  # درصد روزهای مثبت در 12 ماه گذشته
    30: 'days_rank_3_month',  # رتبه روزهای مثبت در 3 ماه گذشته
    31: 'days_rank_12_month',  # رتبه روزهای مثبت در 12 ماه گذشته
}

_STATS_WITH_TRADE_DAYS_INDICES = {
    32: 'days_count_3_month',  # روزهای با معامله در 3 ماه گذشته
    33: 'days_count_12_month',  # روزهای با معامله در 12 ماه گذشته
    34: 'days_rank_3_month',  # رتبه روزهای با معامله در 3 ماه گذشته
    35: 'days_rank_12_month',  # رتبه روزهای با معامله در 12 ماه گذشته
}

_STATS_COMPANY_VALUE_INDICES = {
    36: 'total_value',  # ارزش شرکت در آخرین روز
    37: 'total_value_rank',  # رتبه ارزش شرکت در آخرین روز
}

_STATS_OPEN_DAYS_INDICES = {
    38: 'days_count_3_month',  # تعداد روزهای باز در 3 ماه گذشته
    39: 'days_count_12_month',  # تعداد روزهای باز در 12 ماه گذشته
    40: 'days_percent_3_month',  # درصد روزهای باز در 3 ماه گذشته
    41: 'days_percent_12_month',  # درصد روزهای باز در 12 ماه گذشته
    42: 'days_rank_3_month',  # رتبه روزهای باز در 3 ماه گذشته
    43: 'days_rank_12_month',  # رتبه روزهای باز در 12 ماه گذشته
}

_STATS_CLOSED_DAYS_INDICES = {
    44: 'days_count_3_month',  # تعداد روزهای بسته در 3 ماه گذشته
    45: 'days_count_12_month',  # تعداد روزهای بسته در 12 ماه گذشته
    46: 'days_percent_3_month',  # درصد روزهای بسته در 3 ماه گذشته
    47: 'days_percent_12_month',  # درصد روزهای بسته در 12 ماه گذشته
    48: 'days_rank_3_month',  # رتبه روزهای بسته در 3 ماه گذشته
    49: 'days_rank_12_month',  # رتبه روزهای بسته در 12 ماه گذشته
}

_STATS_CLIENT_TYPE_INDICES = {
    50: 'individual_buy_average_volume_3_month',  # میانگین حجم خرید حقیقی در 3 ماه گذشته
    51: 'individual_buy_average_volume_12_month',  # میانگین حجم خرید حقیقی در 12 ماه گذشته
    52: 'individual_buy_average_volume_rank_3_month',  # رتبه حجم خرید حقیقی در 3 ماه گذشته
    53: 'individual_buy_average_volume_rank_12_month',  # رتبه حجم خرید حقیقی در 12 ماه گذشته
    54: 'legal_buy_average_volume_3_month',  # میانگین حجم خرید حقوقی در 3 ماه گذشته
    55: 'legal_buy_average_volume_12_month',  # میانگین حجم خرید حقوقی در 12 ماه گذشته
    56: 'legal_buy_average_volume_rank_3_month',  # رتبه حجم خرید حقوقی در 3 ماه گذشته
    57: 'legal_buy_average_volume_rank_12_month',  # رتبه حجم خرید حقوقی در 12 ماه گذشته
    58: 'individual_buy_average_count_3_month',  # میانگین تعداد خریدار حقیقی در 3 ماه گذشته
    59: 'individual_buy_average_count_12_month',  # میانگین تعداد خریدار حقیقی در 12 ماه گذشته
    60: 'individual_buy_average_count_rank_3_month',  # رتبه تعداد خریدار حقیقی در 3 ماه گذشته
    61: 'individual_buy_average_count_rank_12_month',  # رتبه تعداد خریدار حقیقی در 12 ماه گذشته
    62: 'legal_buy_average_count_3_month',  # میانگین تعداد خریدار حقوقی در 3 ماه گذشته
    63: 'legal_buy_average_count_12_month',  # میانگین تعداد خریدار حقوقی در 12 ماه گذشته
    64: 'legal_buy_average_count_rank_3_month',  # رتبه تعداد خریدار حقوقی در 3 ماه گذشته
    65: 'legal_buy_average_count_rank_12_month',  # رتبه تعداد خریدار حقوقی در 12 ماه گذشته
    66: 'total_buy_average_count_3_month',  # میانگین تعداد خریداران در 3 ماه گذشته
    67: 'total_buy_average_count_12_month',  # میانگین تعداد خریداران در 12 ماه گذشته
    68: 'total_buy_average_count_rank_3_month',  # رتبه تعداد خریداران در 3 ماه گذشته
    69: 'total_buy_average_count_rank_12_month',  # رتبه تعداد خریداران در 12 ماه گذشته
    70: 'individual_sell_average_volume_3_month',  # میانگین حجم فروش حقیقی در 3 ماه گذشته
    71: 'individual_sell_average_volume_12_month',  # میانگین حجم فروش حقیقی در 12 ماه گذشته
    72: 'individual_sell_average_volume_rank_3_month',  # رتبه حجم فروش حقیقی در 3 ماه گذشته
    73: 'individual_sell_average_volume_rank_12_month',  # رتبه حجم فروش حقیقی در 12 ماه گذشته
    74: 'legal_sell_average_volume_3_month',  # میانگین حجم فروش حقوقی در 3 ماه گذشته
    75: 'legal_sell_average_volume_12_month',  # میانگین حجم فروش حقوقی در 12 ماه گذشته
    76: 'legal_sell_average_volume_rank_3_month',  # رتبه حجم فروش حقوقی در 3 ماه گذشته
    77: 'legal_sell_average_volume_rank_12_month',  # رتبه حجم فروش حقوقی در 12 ماه گذشته
    78: 'individual_sell_average_count_3_month',  # میانگین تعداد فروشنده حقیقی در 3 ماه گذشته
    79: 'individual_sell_average_count_12_month',  # میانگین تعداد فروشنده حقیقی در 12 ماه گذشته
    80: 'individual_sell_average_count_rank_3_month',  # رتبه تعداد فروشنده حقیقی در 3 ماه گذشته
    81: 'individual_sell_average_count_rank_12_month',  # رتبه تعداد فروشنده حقیقی در 12 ماه گذشته
    82: 'legal_sell_average_count_3_month',  # میانگین تعداد فروشنده حقوقی در 3 ماه گذشته
    83: 'legal_sell_average_count_12_month',  # میانگین تعداد فروشنده حقوقی در 12 ماه گذشته
    84: 'legal_sell_average_volume_rank_3_month',  # رتبه تعداد فروشنده حقوقی در 3 ماه گذشته
    85: 'legal_sell_average_volume_rank_12_month',  # رتبه تعداد فروشنده حقوقی در 12 ماه گذشته
    86: 'total_sell_average_count_3_month',  # میانگین تعداد فروشندگان در 3 ماه گذشته
    87: 'total_sell_average_count_12_month',  # میانگین تعداد فروشندگان در 12 ماه گذشته
    88: 'total_sell_average_count_rank_3_month',  # رتبه تعداد فروشندگان در 3 ماه گذشته
    89: 'total_sell_average_count_rank_12_month',  # رتبه تعداد فروشندگان در 12 ماه گذشته
}


def get_watch_price_data(refid: int = 0, heven: int = 0) -> tuple[dict, int, int]:
    response = requests.get(
        url='http://members.tsetmc.com/tsev2/data/MarketWatchInit.aspx',
        params={
            'h': heven,
            'r': refid,
        },
        verify=False,
        timeout=20,
    )
    response.raise_for_status()
    response = response.text

    sections = response.split('@')

    max_heven = 0
    watch_data = {}

    # prices
    rows = sections[2].split(';')
    for row in rows:
        if not row:
            continue

        cols = row.split(',')
        if len(cols) in [0, 10]:
            continue

        symbol_id = cols[0]
        heven = int(cols[4])

        watch_data[symbol_id] = {
            'symbol_id': cols[0],
            'isin': cols[1],
            'short_name': cols[2],
            'full_name': cols[3],
            'heven': int(cols[4]),
            'open': int(cols[5]),
            'close': int(cols[6]),
            'last': int(cols[7]),
            'count': int(cols[8]),
            'volume': int(cols[9]),
            'value': int(cols[10]),
            'low': int(cols[11]),
            'high': int(cols[12]),
            'yesterday': int(cols[13]),
            'eps': int(cols[14]) if cols[14] else None,
            'base_volume': int(cols[15]),
            'visit_count': int(cols[16]),
            'flow': int(cols[17]),
            'group': int(cols[18]),
            'range_max': int(float(cols[19])),
            'range_min': int(float(cols[20])),
            'z': int(cols[21]),
            'yval': int(cols[22]),
            'orderbook': {
                'buy_rows': {},
                'sell_rows': {},
            }
        }

        if heven > max_heven:
            max_heven = heven

    # orderbook
    rows = sections[3].split(';')
    for row in rows:
        if not row:
            continue

        symbol_id, rank, s_count, b_count, b_price, s_price, b_volume, s_volume = row.split(',')

        if symbol_id not in watch_data:
            watch_data[symbol_id] = {
                'orderbook': {
                    'buy_rows': {},
                    'sell_rows': {},
                }
            }

        watch_data[symbol_id]['orderbook']['buy_rows'][int(rank)] = {
            'count': int(b_count),
            'price': int(b_price),
            'volume': int(b_volume),
        }
        watch_data[symbol_id]['orderbook']['sell_rows'][int(rank)] = {
            'count': int(s_count),
            'price': int(s_price),
            'volume': int(s_volume),
        }

    # refid
    refid = int(sections[4])

    return watch_data, refid, max_heven


def get_watch_traders_type_data() -> dict:
    response = requests.get(
        url='http://www.tsetmc.com/tsev2/data/ClientTypeAll.aspx',
        params={},
        verify=False,
        timeout=20,
    )
    response.raise_for_status()
    response = response.text

    watch_data = {}

    rows = response.split(';')
    for row in rows:
        if not row:
            continue

        (
            symbol_id,
            r_buy_c, l_buy_c, r_buy_v, l_buy_v,
            r_sell_c, l_sell_c, r_sell_v, l_sell_v,
        ) = row.split(',')

        watch_data[symbol_id] = {
            'legal': {
                'buy': {
                    'volume': l_buy_v,
                    'count': l_buy_c,
                },
                'sell': {
                    'volume': l_sell_v,
                    'count': l_sell_c,
                }
            },
            'real': {
                'buy': {
                    'volume': r_buy_v,
                    'count': r_buy_c,
                },
                'sell': {
                    'volume': r_sell_v,
                    'count': r_sell_c,
                }
            },
        }

    return watch_data


def get_watch_daily_history_data() -> dict:
    response = requests.get(
        url='http://members.tsetmc.com/tsev2/data/ClosingPriceAll.aspx',
        params={},
        verify=False,
        timeout=20,
    )
    response.raise_for_status()
    response = response.text

    watch_data = defaultdict(list)

    symbol_id = None
    rows = response.split(';')
    for row in rows:
        if not row:
            continue

        row = row.split(',')

        if len(row) == 11:
            symbol_id = row[0]
            row = row[1:]

        day, close, last, count, volume, value, low, high, yesterday, opn = row
        watch_data[symbol_id].append({
            'day': int(day),
            'close': int(close),
            'last': int(last),
            'count': int(count),
            'volume': int(volume),
            'value': int(value),
            'low': int(low),
            'high': int(high),
            'yesterday': int(yesterday),
            'open': int(opn),
        })

    return watch_data


def get_watch_raw_stats_data() -> dict:
    response = requests.get(
        url='http://www.tsetmc.com/tsev2/data/InstValue.aspx?t=a',
        params={},
        verify=False,
        timeout=20,
    )
    response.raise_for_status()
    response = response.text

    symbol_id = None
    ret = defaultdict(dict)
    sections = response.split(';')
    for section in sections:
        r = section.split(',')
        if len(r) == 3:
            symbol_id = r[0]
            r = r[1:]

        index = int(r[0])
        val = int(r[1]) if '.' not in r[1] else float(r[1])

        ret[symbol_id][index] = val

    return ret


def get_watch_stats_data() -> dict:
    raw_stats = get_watch_raw_stats_data()

    ret = {}
    for symbol_id, stats in raw_stats.items():
        ret[symbol_id] = {
            'trades': {},
            'negative_days': {},
            'no_trade_days': {},
            'positive_days': {},
            'with_trade_days': {},
            'company_value': {},
            'open_days': {},
            'closed_days': {},
            'client_type': {},
        }
        for index, val in stats.items():
            if 1 <= index < 18:
                sub_name = 'trades'
                indices_obj = _STATS_TRADES_INDICES
            elif 18 <= index < 24:
                sub_name = 'negative_days'
                indices_obj = _STATS_NEGATIVE_DAYS_INDICES
            elif 24 <= index < 26:
                sub_name = 'no_trade_days'
                indices_obj = _STATS_NO_TRADE_DAYS_INDICES
            elif 26 <= index < 32:
                sub_name = 'positive_days'
                indices_obj = _STATS_POSITIVE_DAYS_INDICES
            elif 32 <= index < 36:
                sub_name = 'with_trade_days'
                indices_obj = _STATS_WITH_TRADE_DAYS_INDICES
            elif 36 <= index < 38:
                sub_name = 'company_value'
                indices_obj = _STATS_COMPANY_VALUE_INDICES
            elif 38 <= index < 44:
                sub_name = 'open_days'
                indices_obj = _STATS_OPEN_DAYS_INDICES
            elif 44 <= index < 50:
                sub_name = 'closed_days'
                indices_obj = _STATS_CLOSED_DAYS_INDICES
            elif 50 <= index < 90:
                sub_name = 'client_type'
                indices_obj = _STATS_CLIENT_TYPE_INDICES
            else:
                continue

            ret[symbol_id][sub_name][indices_obj[index]] = val

    return ret
