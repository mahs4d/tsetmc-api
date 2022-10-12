from tsetmc_api_new.symbol.symbol import Symbol

symbol = Symbol(symbol_id='46348559193224090')

price_overview = symbol.get_traders_type_history()

print(price_overview[0])
