from collections import defaultdict

import requests


def get_watch_price_data(refid: int = 0, heven: int = 0) -> tuple[dict, int, int]:
    response = requests.get(
        url='http://members.tsetmc.com/tsev2/data/MarketWatchInit.aspx',
        params={
            'h': heven,
            'r': refid,
        },
        verify=False,
    )
    response.raise_for_status()
    response = response.text

    sections = response.split('@')

    min_heven = 0
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
            'open_price': int(cols[5]),
            'close_price': int(cols[6]),
            'last_price': int(cols[7]),
            'count': int(cols[8]),
            'volume': int(cols[9]),
            'value': int(cols[10]),
            'low_price': int(cols[11]),
            'high_price': int(cols[12]),
            'yesterday': int(cols[13]),
            'eps': int(cols[14]) if cols[14] else None,
            'base_volume': int(cols[15]),
            'visit_count': int(cols[16]),
            'flow': int(cols[17]),
            'group': int(cols[18]),
            'max_price': int(float(cols[19])),
            'min_price': int(float(cols[20])),
            'z': int(cols[21]),
            'yval': int(cols[22]),
            'orderbook': {
                'buy_rows': {},
                'sell_rows': {},
            }
        }

        if heven < min_heven:
            min_heven = heven

    # orderbook
    rows = sections[3].split(';')
    for row in rows:
        if not row:
            continue

        symbol_id, rank, s_count, b_count, b_price, s_price, b_volume, s_volume = row.split(',')

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

    return watch_data, refid, min_heven


def get_watch_traders_type_data() -> dict:
    response = requests.get(
        url='http://www.tsetmc.com/tsev2/data/ClientTypeAll.aspx',
        params={},
        verify=False,
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
    )
    response.raise_for_status()
    response = response.text

    watch_data = defaultdict(list)

    symbol_id = None
    rows = response.split(';')
    for row in rows:
        if not row:
            continue

        if len(row) == 11:
            symbol_id = row[0]
            row = row[1:]

        close, last, count, volume, value, low, high, yesterday, opn = row
        watch_data[symbol_id].append({
            'close': close,
            'last': last,
            'count': count,
            'volume': volume,
            'value': value,
            'low': low,
            'high': high,
            'yesterday': yesterday,
            'open': opn,
        })

    return watch_data
