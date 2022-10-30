import requests


def get_market_map_data(map_type: int, heven: int = 0) -> tuple[dict[dict], int]:
    response = requests.get(
        url='http://cdn.tsetmc.com/api/ClosingPrice/GetMarketMap',
        params={
            'market': 0,
            'size': 1920,
            'sector': 0,
            'typeSelected': map_type,
            'hEven': heven,
        },
        verify=False,
        timeout=20,
    )
    response.raise_for_status()
    response = response.json()

    min_heven = 0
    watch_data = {}
    for row in response:
        symbol_id = row['insCode']
        min_heven = min(row['hEven'], min_heven)
        watch_data[symbol_id] = {
            'symbol_id': row['insCode'],
            'color': row['color'],
            'symbol_short_name': row['lVal18AFC'],
            'symbol_long_name': row['lVal30'],
            'group_name': row['lSecVal'],
            'close': row['pClosing'],
            'last': row['pDrCotVal'],
            'percent': row['percent'],
            'price_change_percent': row['priceChangePercent'],
            'volume': row['qTotTran5J'],
            'value': row['qTotCap'],
            'count': row['zTotTran'],
        }

    return watch_data, min_heven
