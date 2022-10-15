import requests


def get_market_map_data(map_type: int) -> list[dict]:
    response = requests.get(
        url='http://cdn.tsetmc.com/api/ClosingPrice/GetMarketMap',
        params={
            'market': 0,
            'size': 1920,
            'sector': 0,
            'typeSelected': map_type,
            'hEven': 0,
        },
        verify=False,
    )
    response.raise_for_status()
    response = response.json()

    return [{
        'color': row['color'],
        'symbol_id': row['insCode'],
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
    } for row in response]
