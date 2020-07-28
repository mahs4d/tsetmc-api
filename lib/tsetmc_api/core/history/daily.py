from datetime import date

import requests


def load_daily_history_data(asset_id, limit=999999):
    """
    سابقه‌ی نماد (نماد >‌ سابقه)
    """

    daily_content = requests.get(
        f'http://members.tsetmc.com/tsev2/data/InstTradeHistory.aspx?i={asset_id}&Top={limit}&A=0',
        timeout=20).text
    raw_ticks = daily_content.split(';')

    ticks = []
    for raw_tick in raw_ticks:
        if raw_tick == '':
            continue

        tick_data = raw_tick.split('@')

        date_raw = tick_data[0]
        high_price = tick_data[1]
        low_price = tick_data[2]
        close_price = tick_data[3]
        last_price = tick_data[4]
        first_price = tick_data[5]
        yesterday_price = tick_data[6]
        value = tick_data[7]
        volume = tick_data[8]

        ticks.append({
            'date': date(year=int(date_raw[:4]), month=int(date_raw[4:6]), day=int(date_raw[6:])),
            'first_price': int(first_price[:-3]),
            'high_price': int(high_price[:-3]),
            'low_price': int(low_price[:-3]),
            'close_price': int(close_price[:-3]),
            'last_price': int(last_price[:-3]),
            'yesterday_price': int(yesterday_price[:-3]),
            'value': int(float(value)),
            'volume': int(float(volume)),
        })

    return ticks
