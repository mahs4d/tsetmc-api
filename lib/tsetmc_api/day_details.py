from dateutil import tz as timezoneutil
from jdatetime import date, time

from .core import day_details as day_details_core
from .core.cache import PersistentCache
from .shareholder import AssetMajorShareholder

_timezone = timezoneutil.gettz('Asia/Tehran')


def _i_to_time(i):
    if isinstance(i, str):
        x = i
    else:
        x = str(i)

    if len(x) != 5:
        h = int(x[:2])
        m = int(x[2:4])
        s = int(x[4:])
    else:
        h = int(x[:1])
        m = int(x[1:3])
        s = int(x[3:])

    return time(hour=h, minute=m, second=s, tzinfo=_timezone)


def _create_snapshot(price_data, orders_data, distinct=True):
    max_t = price_data['t']
    snapshot = {
        'time': max_t,
        'last': price_data['lst'],
        'yesterday': price_data['y'],
        'open': price_data['o'],
        'high': price_data['h'],
        'close': price_data['c'],
        'low': price_data['l'],
        'count': price_data['cnt'],
        'volume': price_data['v'],
        'state': price_data['s'],
    } if distinct else price_data

    buy_orders = []
    sell_orders = []
    for to in orders_data:
        if to is not None:
            buy_orders.append({
                'time': _i_to_time(to['t']),
                'count': to['bcnt'],
                'volume': to['bv'],
                'price': to['bp'],
            })
            sell_orders.append({
                'time': _i_to_time(to['t']),
                'count': to['scnt'],
                'volume': to['sv'],
                'price': to['sp'],
            })

            max_t = max(max_t, to['t'])

    snapshot['time'] = _i_to_time(max_t)
    snapshot['buy_orders'] = buy_orders
    snapshot['sell_orders'] = sell_orders

    return snapshot


def _generate_snapshot_data(price_data, orders_data):
    max_pdi = len(price_data)
    max_odi = len(orders_data)
    pdi = 0
    odi = -1
    last_price_data = price_data[pdi]
    last_orders_data = [None, None, None]

    while True:
        phase = -1
        if pdi + 1 < max_pdi and odi + 1 < max_odi:
            if price_data[pdi + 1]['t'] < orders_data[odi + 1]['t']:
                phase = 1
            elif price_data[pdi + 1]['t'] > orders_data[odi + 1]['t']:
                phase = 2
            else:
                phase = 3
        else:
            if pdi + 1 == max_pdi and odi + 1 == max_odi:
                break
            elif pdi + 1 < max_pdi:
                phase = 1
            elif odi + 1 < max_odi:
                phase = 2

        # step price data and use the old order data
        if phase == 1 or phase == 3:
            pdi += 1
            last_price_data = price_data[pdi]

        # step orders
        if phase == 2 or phase == 3:
            t = orders_data[odi + 1]['t']
            orders_found = [None, None, None]
            while True:
                if odi + 1 >= max_odi:
                    break

                order = orders_data[odi + 1]
                rank = min(order['rank'] - 1, 2)
                if orders_found[rank] is not None or order['t'] > t:
                    break

                odi += 1
                orders_found[rank] = order
                last_orders_data[rank] = order

        yield _create_snapshot(last_price_data, last_orders_data)


class AssetDayDetails:
    def __init__(self, asset, jyear, jmonth, jday):
        self.asset = asset
        self.date = date(year=jyear, month=jmonth, day=jday)

        self._load()

    def _load(self):
        cache_minor = f'{self.asset.id}-{self.date.year}-{self.date.month}-{self.date.day}'
        if PersistentCache.exists('asset_day_details', cache_minor):
            f = PersistentCache.fetch('asset_day_details', cache_minor)
            self._final_shareholders = f['final_shareholders']
            self._initial_shareholders = f['initial_shareholders']
            self._trades = f['trades']
            self._snapshots = f['snapshots']
            return

        mdate = self.date.togregorian()
        data = day_details_core.load_intraday_data(self.asset.id, mdate.year, mdate.month, mdate.day)
        asset_details = self.asset.get_details()

        self._final_shareholders = []
        for shdata in data['shareholders']:
            self._final_shareholders.append(AssetMajorShareholder(self.asset.id,
                                                                  company_isin=asset_details['company_isin'],
                                                                  holder_name=shdata['name'],
                                                                  holder_id=shdata['id'],
                                                                  percentage=shdata['percentage'],
                                                                  shares_count=shdata['shares_count']))

        self._initial_shareholders = []
        for shdata in data['yesterday_shareholders']:
            self._initial_shareholders.append(AssetMajorShareholder(self.asset.id,
                                                                    company_isin=asset_details['company_isin'],
                                                                    holder_name=shdata['name'],
                                                                    holder_id=shdata['id'],
                                                                    percentage=shdata['percentage'],
                                                                    shares_count=shdata['shares_count']))

        self._trades = []
        for tdata in data['trades']:
            self._trades.append({
                'order': tdata['order'],
                'volume': tdata['v'],
                'price': tdata['p'],
                'time': _i_to_time(tdata['t']),
            })

        self._snapshots = list(_generate_snapshot_data(data['price_data'], data['orders_data']))

        PersistentCache.store('asset_day_details', cache_minor, {
            'final_shareholders': self._final_shareholders,
            'initial_shareholders': self._initial_shareholders,
            'trades': self._trades,
            'snapshots': self._snapshots,
        })

    def get_final_major_shareholders(self):
        """
        سهامداران عمده در پایان روز
        """
        return self._final_shareholders

    def get_initial_major_shareholders(self):
        """
        سهامداران عمده در ابتدای روز
        """
        return self._initial_shareholders

    def get_trades(self):
        """
        معاملات
        """
        return self._trades

    def get_snapshots(self):
        """
        تمام لحظات سهم در طور روز
        """
        return self._snapshots

    def get_snapshots_by_time(self, hour, minute, second):
        """
        وضعیت سهم در زمان خاصی از روز
        """
        snapshots = []
        t = time(hour=hour, minute=minute, second=second, tzinfo=_timezone)
        last_snapshot = None
        for snapshot in self._snapshots:
            if snapshot['time'] > t:
                if not snapshots:
                    return [last_snapshot]

                return snapshots

            if snapshot['time'] == t:
                snapshots.append(snapshot)

            last_snapshot = snapshot

        if not snapshots:
            return [last_snapshot]

        return snapshots

    def get_ticks(self, tick_length):
        """
        وضعیت سهم در لحظات مختلف روز در بازه‌هایی با طول tick_length
        """
        # todo
        raise NotImplementedError('sorry, ticks are not supported yet :(')

    def __str__(self):
        return f'AssetDayDetails > {self.asset.id} @ {self.date}'
