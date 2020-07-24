import time

import requests

from .asset import Asset


def _decompile_price_section(raw_section):
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
            'asset': Asset(asset_id, short_name, full_name, isin),
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
            'visits': visit_count,
            'flow': flow,
            'group': group,
            'max': max_price,
            'min': min_price,
            'z': z,
            'yval': yval,
            'buy_orders': [],
            'sell_orders': [],
        }

    return ret


def _decompile_orders_section(raw_section, watch):
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
            'rank': rank,
            'count': buy_count,
            'price': buy_price,
            'volume': buy_volume,
        })
        ainfo['sell_orders'].append({
            'rank': rank,
            'count': sell_count,
            'price': sell_price,
            'volume': sell_volume,
        })

    return watch


def _fetch_raw_ticks_data():
    r = requests.get('http://www.tsetmc.com/tsev2/data/MarketWatchInit.aspx?h=0&r=0')
    r.raise_for_status()

    raw_data = r.text
    sections = raw_data.split('@')

    watch = _decompile_price_section(sections[2])
    watch = _decompile_orders_section(sections[3], watch)
    refid = sections[4]

    return watch, refid


class Ticks:
    def __init__(self, raw_ticks_data):
        self.raw_ticks_data = raw_ticks_data

    def get_by_asset(self, asset_id):
        return self.raw_ticks_data[asset_id]

    def get_all(self):
        return self.raw_ticks_data.values()


class Ticker:
    def __init__(self, watch_refresh_rate=1):
        self._watch_refresh_rate = watch_refresh_rate

        self._bindings = []

    def bind(self, listener):
        self._bindings.append({
            'listener': listener
        })

    def start(self):
        while True:
            time.sleep(self._watch_refresh_rate)
            raw_ticks_data, _ = _fetch_raw_ticks_data()
            ticks = Ticks(raw_ticks_data)

            for binding in self._bindings:
                binding['listener'](ticks)
