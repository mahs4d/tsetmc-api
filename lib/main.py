from tsetmc_api_new.market_map import map
from tsetmc_api_new.market_map.map import MapType
from tsetmc_api_new.symbol.symbol import Symbol

m = map.MarketMap()
print(m.get_market_map_tick(map_type=MapType.MARKET_VOLUME))

# symbol = Symbol(symbol_id='46348559193224090')
#
# price_overview = symbol.get_traders_type_history()
#
# print(price_overview[0])
