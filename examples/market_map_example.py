from tsetmc_api.market_map import MarketMap, MapType

# نقشه‌ی بازار
market_map = MarketMap()

# گرفتن نقشه‌ی بازار بر اساس ارزش
map_by_value = market_map.get_market_map_data(map_type=MapType.MARKET_VALUE)

# گرفتن نقشه‌ی بازار بر اساس حجم
map_by_volume = market_map.get_market_map_data(map_type=MapType.MARKET_VOLUME)
