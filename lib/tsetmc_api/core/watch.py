import requests


def _extract_prices(raw_section):
    ret = {}

    rows = raw_section.split(';')
    for row in rows:
        if row == '':
            continue

        cols = row.split(',')
        if len(cols) in [0, 10]:
            continue

        asset_id = cols[0]
        isin = cols[1]
        short_name = cols[2]
        full_name = cols[3]
        open_price = int(cols[5])
        close_price = int(cols[6])
        last_price = int(cols[7])
        count = int(cols[8])
        volume = int(cols[9])
        value = int(cols[10])
        low_price = int(cols[11])
        high_price = int(cols[12])
        yesterday = int(cols[13])
        eps = int(cols[14]) if cols[14] != '' else None
        base_volume = int(cols[15])
        visit_count = int(cols[16])
        flow = int(cols[17])
        group = int(cols[18])
        max_price = int(float(cols[19]))
        min_price = int(float(cols[20]))
        z = int(cols[21])
        yval = int(cols[22])

        ret[asset_id] = {
            'asset_id': asset_id,
            'symbol_short_name': short_name,
            'symbol_long_name': full_name,
            'isin': isin,
            'open': open_price,
            'close': close_price,
            'last': last_price,
            'high': high_price,
            'low': low_price,
            'count': count,
            'volume': volume,
            'value': value,
            'yesterday': yesterday,
            'eps': eps,
            'base_volume': base_volume,
            'visits_count': visit_count,
            'flow': flow,
            'group_code': group,
            'max': max_price,
            'min': min_price,
            'z': z,
            'yval': yval,
            'buy_orders': [],
            'sell_orders': [],
        }

    return ret


def _extract_orders(raw_section, watch):
    ret = {}
    rows = raw_section.split(';')
    for row in rows:
        if row == '':
            continue

        cols = row.split(',')

        asset_id = cols[0]
        rank = cols[1]
        sell_count = cols[2]
        buy_count = cols[3]
        buy_price = cols[4]
        sell_price = cols[5]
        buy_volume = cols[6]
        sell_volume = cols[7]

        ainfo = watch.get(asset_id, None)
        if ainfo is None:
            continue
        ainfo['buy_orders'].append({
            'rank': int(rank),
            'count': int(buy_count),
            'price': int(buy_price),
            'volume': int(buy_volume),
        })
        ainfo['sell_orders'].append({
            'rank': int(rank),
            'count': int(sell_count),
            'price': int(sell_price),
            'volume': int(sell_volume),
        })

        ret[asset_id] = ainfo

    return ret


def fetch_watch_simple_data():
    r = requests.get('http://www.tsetmc.com/tsev2/data/MarketWatchInit.aspx?h=0&r=0')
    r.raise_for_status()

    raw_data = r.text
    sections = raw_data.split('@')

    watch = _extract_prices(sections[2])
    watch = _extract_orders(sections[3], watch)
    refid = sections[4]

    return watch, refid


def fetch_watch_client_type_data():
    r = requests.get('http://www.tsetmc.com/tsev2/data/ClientTypeAll.aspx')
    r.raise_for_status()
    raw_data = r.text

    ret = {}
    sections = raw_data.split(';')
    for section in sections:
        r = section.split(',')
        asset_id = r[0]
        ret[asset_id] = {
            'natural': {
                'buy_count': int(r[1]),
                'buy_volume': int(r[3]),
                'sell_count': int(r[5]),
                'sell_volume': int(r[7]),
            },
            'legal': {
                'buy_count': int(r[2]),
                'buy_volume': int(r[4]),
                'sell_count': int(r[6]),
                'sell_volume': int(r[8]),
            },
        }

    return ret


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
    50: 'natural_buy_average_volume_3_month',  # میانگین حجم خرید حقیقی در 3 ماه گذشته
    51: 'natural_buy_average_volume_12_month',  # میانگین حجم خرید حقیقی در 12 ماه گذشته
    52: 'natural_buy_average_volume_rank_3_month',  # رتبه حجم خرید حقیقی در 3 ماه گذشته
    53: 'natural_buy_average_volume_rank_12_month',  # رتبه حجم خرید حقیقی در 12 ماه گذشته
    54: 'legal_buy_average_volume_3_month',  # میانگین حجم خرید حقوقی در 3 ماه گذشته
    55: 'legal_buy_average_volume_12_month',  # میانگین حجم خرید حقوقی در 12 ماه گذشته
    56: 'legal_buy_average_volume_rank_3_month',  # رتبه حجم خرید حقوقی در 3 ماه گذشته
    57: 'legal_buy_average_volume_rank_12_month',  # رتبه حجم خرید حقوقی در 12 ماه گذشته
    58: 'natural_buy_average_count_3_month',  # میانگین تعداد خریدار حقیقی در 3 ماه گذشته
    59: 'natural_buy_average_count_12_month',  # میانگین تعداد خریدار حقیقی در 12 ماه گذشته
    60: 'natural_buy_average_count_rank_3_month',  # رتبه تعداد خریدار حقیقی در 3 ماه گذشته
    61: 'natural_buy_average_count_rank_12_month',  # رتبه تعداد خریدار حقیقی در 12 ماه گذشته
    62: 'legal_buy_average_count_3_month',  # میانگین تعداد خریدار حقوقی در 3 ماه گذشته
    63: 'legal_buy_average_count_12_month',  # میانگین تعداد خریدار حقوقی در 12 ماه گذشته
    64: 'legal_buy_average_count_rank_3_month',  # رتبه تعداد خریدار حقوقی در 3 ماه گذشته
    65: 'legal_buy_average_count_rank_12_month',  # رتبه تعداد خریدار حقوقی در 12 ماه گذشته
    66: 'total_buy_average_count_3_month',  # میانگین تعداد خریداران در 3 ماه گذشته
    67: 'total_buy_average_count_12_month',  # میانگین تعداد خریداران در 12 ماه گذشته
    68: 'total_buy_average_count_rank_3_month',  # رتبه تعداد خریداران در 3 ماه گذشته
    69: 'total_buy_average_count_rank_12_month',  # رتبه تعداد خریداران در 12 ماه گذشته
    70: 'natural_sell_average_volume_3_month',  # میانگین حجم فروش حقیقی در 3 ماه گذشته
    71: 'natural_sell_average_volume_12_month',  # میانگین حجم فروش حقیقی در 12 ماه گذشته
    72: 'natural_sell_average_volume_rank_3_month',  # رتبه حجم فروش حقیقی در 3 ماه گذشته
    73: 'natural_sell_average_volume_rank_12_month',  # رتبه حجم فروش حقیقی در 12 ماه گذشته
    74: 'legal_sell_average_volume_3_month',  # میانگین حجم فروش حقوقی در 3 ماه گذشته
    75: 'legal_sell_average_volume_12_month',  # میانگین حجم فروش حقوقی در 12 ماه گذشته
    76: 'legal_sell_average_volume_rank_3_month',  # رتبه حجم فروش حقوقی در 3 ماه گذشته
    77: 'legal_sell_average_volume_rank_12_month',  # رتبه حجم فروش حقوقی در 12 ماه گذشته
    78: 'natural_sell_average_count_3_month',  # میانگین تعداد فروشنده حقیقی در 3 ماه گذشته
    79: 'natural_sell_average_count_12_month',  # میانگین تعداد فروشنده حقیقی در 12 ماه گذشته
    80: 'natural_sell_average_count_rank_3_month',  # رتبه تعداد فروشنده حقیقی در 3 ماه گذشته
    81: 'natural_sell_average_count_rank_12_month',  # رتبه تعداد فروشنده حقیقی در 12 ماه گذشته
    82: 'legal_sell_average_count_3_month',  # میانگین تعداد فروشنده حقوقی در 3 ماه گذشته
    83: 'legal_sell_average_count_12_month',  # میانگین تعداد فروشنده حقوقی در 12 ماه گذشته
    84: 'legal_sell_average_volume_rank_3_month',  # رتبه تعداد فروشنده حقوقی در 3 ماه گذشته
    85: 'legal_sell_average_volume_rank_12_month',  # رتبه تعداد فروشنده حقوقی در 12 ماه گذشته
    86: 'total_sell_average_count_3_month',  # میانگین تعداد فروشندگان در 3 ماه گذشته
    87: 'total_sell_average_count_12_month',  # میانگین تعداد فروشندگان در 12 ماه گذشته
    88: 'total_sell_average_count_rank_3_month',  # رتبه تعداد فروشندگان در 3 ماه گذشته
    89: 'total_sell_average_count_rank_12_month',  # رتبه تعداد فروشندگان در 12 ماه گذشته
}


def fetch_watch_stats_data():
    r = requests.get('http://www.tsetmc.com/tsev2/data/InstValue.aspx?t=a')
    r.raise_for_status()
    raw_data = r.text

    asset_id = None
    ret = {}
    sections = raw_data.split(';')
    for section in sections:
        r = section.split(',')
        x = 0
        if len(r) == 3:
            asset_id = r[0]
            x = 1

        index = int(r[x + 0])
        val = int(r[x + 1]) if '.' not in r[x + 1] else float(r[x + 1])
        if asset_id not in ret:
            ret[asset_id] = {
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

        sub_name = None
        indices_obj = None

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

        ret[asset_id][sub_name][indices_obj[index]] = val

    return ret


def fetch_watch_historical_data():
    r = requests.get('http://members.tsetmc.com/tsev2/data/ClosingPriceAll.aspx')
    r.raise_for_status()
    raw_data = r.text

    asset_id = None
    ret = {}
    sections = raw_data.split(';')
    for section in sections:
        r = section.split(',')
        x = 0
        if len(r) == 11:
            asset_id = r[0]

            x = 1

        index = int(r[x + 0])
        if asset_id not in ret:
            ret[asset_id] = {}
        ret[asset_id][index] = {
            'close': int(r[x + 1]),
            'last': int(r[x + 2]),
            'count': int(r[x + 3]),
            'volume': int(r[x + 4]),
            'value': int(r[x + 5]),
            'low': int(r[x + 6]),
            'high': int(r[x + 7]),
            'yesterday': int(r[x + 8]),
            'open': int(r[x + 9]),
        }

    return ret
