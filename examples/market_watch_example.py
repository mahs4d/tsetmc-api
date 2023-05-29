from tsetmc_api.market_watch import MarketWatch


def method_sync():
	# دیده‌بان بازار
	# توجه کنید که این اطلاعات از صفحه‌ی دیده‌بان بازاره و مثلا سابقه‌ی اینجا با اون سابقه‌ای که توی صفحه
	# نماد می‌بینیم فرق داره. اونا توی پکیج symbol قرار دارند.
	market_watch = MarketWatch()
	
	# اطلاعات قیمتی
	price_data = market_watch.get_price_data()
	print(f'price data({len(price_data)}):\n', '\n'.join(f'\t {k}: {v}' for k, v in list(price_data.items())[-5:]))

	# اطلاعات آماری به صورت خام
	raw_stats_data = market_watch.get_raw_stats_data()
	print(f'raw stats data({len(raw_stats_data)}):\n', '\n'.join(f'\t {k}: {v}' for k, v in list(raw_stats_data.items())[-5:]))

	# اطلاعات آماری به صورت parse شده
	stats_data = market_watch.get_stats_data()
	print(f'stats data({len(stats_data)}):\n', '\n'.join(f'\t {k}: {v}' for k, v in list(stats_data.items())[-5:]))

	# اطلاعات حقیقی حقوقی
	traders_type_data = market_watch.get_traders_type_data()
	print(f'traders type data({len(traders_type_data)}):\n', '\n'.join(f'\t {k}: {v}' for k, v in list(traders_type_data.items())[-5:]))

	# اطلاعات سابقه
	daily_history_data = market_watch.get_daily_history_data()
	print(f'daily history data({len(daily_history_data)}):\n', '\n'.join(f'\t {k}: {v}' for k, v in list(daily_history_data.items())[-5:]))


async def method_async():
	# دیده‌بان بازار
	# توجه کنید که این اطلاعات از صفحه‌ی دیده‌بان بازاره و مثلا سابقه‌ی اینجا با اون سابقه‌ای که توی صفحه
	# نماد می‌بینیم فرق داره. اونا توی پکیج symbol قرار دارند.
	market_watch = MarketWatch()
	
	# اطلاعات قیمتی
	price_data = await market_watch.aio_get_price_data()
	print(f'price data({len(price_data)}):\n', '\n'.join(f'\t {k}: {v}' for k, v in list(price_data.items())[-5:]))
	
	# اطلاعات آماری به صورت خام
	raw_stats_data = await market_watch.aio_get_raw_stats_data()
	print(f'raw stats data({len(raw_stats_data)}):\n', '\n'.join(f'\t {k}: {v}' for k, v in list(raw_stats_data.items())[-5:]))
	
	# اطلاعات آماری به صورت parse شده
	stats_data = await market_watch.aio_get_stats_data()
	print(f'stats data({len(stats_data)}):\n', '\n'.join(f'\t {k}: {v}' for k, v in list(stats_data.items())[-5:]))
	
	# اطلاعات حقیقی حقوقی
	traders_type_data = await market_watch.aio_get_traders_type_data()
	print(f'traders type data({len(traders_type_data)}):\n', '\n'.join(f'\t {k}: {v}' for k, v in list(traders_type_data.items())[-5:]))
	
	# اطلاعات سابقه
	daily_history_data = await market_watch.aio_get_daily_history_data()
	print(f'daily history data({len(daily_history_data)}):\n', '\n'.join(f'\t {k}: {v}' for k, v in list(daily_history_data.items())[-5:]))


if __name__ == '__main__':
	print('RunMode: Sync')
	method_sync()
	
	print('RunMode: Async')
	
	from asyncio import run
	
	run(method_async())
