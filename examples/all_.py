from examples import (
	day_details_example,
	group_example,
	market_map_example,
	market_watch_example,
	symbol_example
)
from asyncio import run

if __name__ == '__main__':
	print('*' * 50, 'day_details_example RunMode: Sync', '*' * 50)
	day_details_example.method_sync()
	print('*' * 50, 'group_example RunMode: Sync', '*' * 50)
	group_example.method_sync()
	print('*' * 50, 'market_map_example RunMode: Sync', '*' * 50)
	market_map_example.method_sync()
	print('*' * 50, 'market_watch_example RunMode: Sync', '*' * 50)
	market_watch_example.method_sync()
	print('*' * 50, 'symbol_example RunMode: Sync', '*' * 50)
	symbol_example.method_sync()
	
	print('*' * 50, 'day_details_example RunMode: Async', '*' * 50)
	run(day_details_example.method_async())
	print('*' * 50, 'group_example RunMode: Async', '*' * 50)
	run(group_example.method_async())
	print('*' * 50, 'market_map_example RunMode: Async', '*' * 50)
	run(market_map_example.method_async())
	print('*' * 50, 'market_watch_example RunMode: Async', '*' * 50)
	run(market_watch_example.method_async())
	print('*' * 50, 'symbol_example RunMode: Async', '*' * 50)
	run(symbol_example.method_async())
