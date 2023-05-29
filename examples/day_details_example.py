from jdatetime import date as jdate

from tsetmc_api.day_details import DayDetails


def method_sync():
	# تغییرات نماد در یک روز
	day_details = DayDetails(symbol_id='14079693677610396', date=jdate(1402, 3, 1))
	
	# قیمت‌های نهایی
	price_overview = day_details.get_price_overview()
	print('price overview: \n\t', price_overview)
	
	# تغییرات قیمتی
	price_data = day_details.get_price_data()
	print(f'price data({len(price_data)}):\n', '\n'.join(f'\t {item}' for item in price_data[-5:]))
	
	# تغییرات صف‌های خرید و فروش
	orderbook_data = day_details.get_orderbook_data()
	print(f'orderbook data({len(orderbook_data)}):\n', '\n'.join(f'\t {item}' for item in orderbook_data[-5:]))
	
	# معاملات
	trades_data = day_details.get_trades_data()
	print(f'trades data({len(trades_data)}):\n', '\n'.join(f'\t {item}' for item in trades_data[-5:]))
	
	# بیشترین و کمترین قیمت روز
	thresholds_data = day_details.get_thresholds_data()
	print('thresholds data: \n\t', thresholds_data)
	
	# تغییرات سهامداران عمده
	old_shareholders, new_shareholders = day_details.get_shareholders_data()
	print(f'share holders old({len(old_shareholders)}):\n', '\n'.join(f'\t {item}' for item in old_shareholders[-5:]))
	print(f'share holders new({len(new_shareholders)}):\n', '\n'.join(f'\t {item}' for item in new_shareholders[-5:]))
	
	if old_shareholders:
		sh = old_shareholders[0]
	elif new_shareholders:
		sh = new_shareholders[0]
	else:
		print('no share holders')
		return
	
	print('share holder details: ', sh.shareholder.name)
	
	# چارت یک سهامدار
	sh_chart_data = sh.get_chart_data()
	print(f'share holder chart data({len(sh_chart_data)}):\n', '\n'.join(f'\t {item}' for item in new_shareholders[-5:]))
	
	# سهام یک سهامدار عمده
	sh_portfolio = sh.shareholder.get_portfolio_data()
	print(f'share holder portfolio data({len(sh_portfolio)}):\n', '\n'.join(f'\t {item}' for item in sh_portfolio[-5:]))


async def method_async():
	# تغییرات نماد در یک روز
	day_details = DayDetails(symbol_id='14079693677610396', date=jdate(1402, 3, 1))
	
	# قیمت‌های نهایی
	price_overview = await day_details.aio_get_price_overview()
	print('price overview: \n\t', price_overview)

	# تغییرات قیمتی
	price_data = await day_details.aio_get_price_data()
	print(f'price data({len(price_data)}):\n', '\n'.join(f'\t {item}' for item in price_data[-5:]))

	# تغییرات صف‌های خرید و فروش
	orderbook_data = await day_details.aio_get_orderbook_data()
	print(f'orderbook data({len(orderbook_data)}):\n', '\n'.join(f'\t {item}' for item in orderbook_data[-5:]))
	
	# معاملات
	trades_data = await day_details.aio_get_trades_data()
	print(f'trades data({len(trades_data)}):\n', '\n'.join(f'\t {item}' for item in trades_data[-5:]))
	
	# بیشترین و کمترین قیمت روز
	thresholds_data = await day_details.aio_get_thresholds_data()
	print('thresholds data: \n\t', thresholds_data)
	
	# تغییرات سهامداران عمده
	old_shareholders, new_shareholders = await day_details.aio_get_shareholders_data()
	print(f'share holders old({len(old_shareholders)}):\n', '\n'.join(f'\t {item}' for item in old_shareholders[-5:]))
	print(f'share holders new({len(new_shareholders)}):\n', '\n'.join(f'\t {item}' for item in new_shareholders[-5:]))
	
	if old_shareholders:
		sh = old_shareholders[0]
	elif new_shareholders:
		sh = new_shareholders[0]
	else:
		print('no share holders')
		return
	
	print('share holder details: ', sh.shareholder.name)
	
	# چارت یک سهامدار
	sh_chart_data = await sh.aio_get_chart_data()
	print(f'share holder chart data({len(sh_chart_data)}):\n', '\n'.join(f'\t {item}' for item in new_shareholders[-5:]))
	
	# سهام یک سهامدار عمده
	sh_portfolio = await sh.shareholder.aio_get_portfolio_data()
	print(f'share holder portfolio data({len(sh_portfolio)}):\n', '\n'.join(f'\t {item}' for item in sh_portfolio[-5:]))


if __name__ == '__main__':
	print('RunMode: Sync')
	method_sync()
	
	print('RunMode: Async')
	
	from asyncio import run
	
	run(method_async())
