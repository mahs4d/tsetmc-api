from tsetmc_api.market_map import MarketMap, MapType


def method_sync():
	# نقشه‌ی بازار
	market_map = MarketMap()
	
	# گرفتن نقشه‌ی بازار بر اساس ارزش
	map_by_value = market_map.get_market_map_data(map_type=MapType.MARKET_VALUE)
	print(f'map by value({len(map_by_value)}):\n', '\n'.join(f'\t {k}: {v}' for k, v in list(map_by_value.items())[-5:]))

	# گرفتن نقشه‌ی بازار بر اساس حجم
	map_by_volume = market_map.get_market_map_data(map_type=MapType.MARKET_VOLUME)
	print(f'map by volume({len(map_by_volume)}):\n', '\n'.join(f'\t {k}: {v}' for k, v in list(map_by_volume.items())[-5:]))


async def method_async():
	# نقشه‌ی بازار
	market_map = MarketMap()
	
	# گرفتن نقشه‌ی بازار بر اساس ارزش
	map_by_value = await market_map.aio_get_market_map_data(map_type=MapType.MARKET_VALUE)
	print(f'map by value({len(map_by_value)}):\n', '\n'.join(f'\t {k}: {v}' for k, v in list(map_by_value.items())[-5:]))
	
	# گرفتن نقشه‌ی بازار بر اساس حجم
	map_by_volume = await market_map.aio_get_market_map_data(map_type=MapType.MARKET_VOLUME)
	print(f'map by volume({len(map_by_volume)}):\n', '\n'.join(f'\t {k}: {v}' for k, v in list(map_by_volume.items())[-5:]))


if __name__ == '__main__':
	print('RunMode: Sync')
	method_sync()
	
	print('RunMode: Async')
	
	from asyncio import run
	
	run(method_async())
