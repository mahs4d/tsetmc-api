from tsetmc_api.symbol import Symbol


def method_sync():
	# دیدن مشخصات یک نماد (نماد آسیاتک)
	# این عددی که به عنوان symbol_id بهش میدیم، از تیکه‌ی آخر url صفحه‌ی آسیاتک توی سایت برداشته شده
	# مثلا آدرس آسیاتک توی tsetmc اینه: http://main.tsetmc.com/InstInfo/14079693677610396
	# اون تیکه آخرش میشه symbol_id
	symbol = Symbol(symbol_id='14079693677610396')
	
	# اطلاعات قیمتی داخل در یک نگاه
	price_overview = symbol.get_price_overview()
	print(f'price overview: \n\t', price_overview)

	# چارت داخل در یک نگاه
	intraday_price_chart_data = symbol.get_intraday_price_chart_data()
	print(f'interaday price chart data({len(intraday_price_chart_data)}):\n', '\n'.join(f'\t {item}' for item in intraday_price_chart_data[-5:]))

	# پیام ناظر
	supervisor_message_data = symbol.get_supervisor_messages_data()
	print(f'supervisor message data({len(supervisor_message_data)}):\n', '\n'.join(f'\t {item}' for item in supervisor_message_data[-5:]))

	# اطلاعیه
	notification_data = symbol.get_notifications_data()
	print(f'notification data({len(notification_data)}):\n', '\n'.join(f'\t {item}' for item in notification_data[-5:]))

	# تغییر وضعیت
	state_changes_data = symbol.get_state_changes_data()
	print(f'state changes data({len(state_changes_data)}):\n', '\n'.join(f'\t {item}' for item in state_changes_data[-5:]))

	# سابقه
	daily_history = symbol.get_daily_history()
	print(f'daily history data({len(daily_history)}):\n', '\n'.join(f'\t {item}' for item in daily_history[-5:]))

	# شناسه
	id_details = symbol.get_id_details()
	print(f'id details: \n\t', id_details)

	# حقیقی حقوقی
	traders_type_history = symbol.get_traders_type_history()
	print(f'traders type history({len(traders_type_history)}):\n', '\n'.join(f'\t {item}' for item in traders_type_history[-5:]))

	# سهامداران
	shareholders = symbol.get_shareholders_data()
	print(f'share holders({len(shareholders)}):\n', '\n'.join(f'\t {item}' for item in shareholders[-5:]))
	
	if shareholders:
		sh = shareholders[0]
		print(f'shareholder info: {sh.shareholder.name}')
	else:
		print('no shareholders found')
		return
	
	# چارتی که وقتی روی یک سهامدار کلیک میکنیم میده
	shareholder_chart_data = sh.get_chart_data()
	print(f'share holder chart data({len(shareholder_chart_data)}):\n', '\n'.join(f'\t {item}' for item in shareholder_chart_data[-5:]))

	# سایر سهام سهامدار عمده
	shareholder_portfolio_data = shareholders[0].shareholder.get_portfolio_data()
	print(f'share holder portfolio data({len(shareholder_portfolio_data)}):\n', '\n'.join(f'\t {item}' for item in shareholder_portfolio_data[-5:]))


async def method_async():
	# دیدن مشخصات یک نماد (نماد آسیاتک)
	# این عددی که به عنوان symbol_id بهش میدیم، از تیکه‌ی آخر url صفحه‌ی آسیاتک توی سایت برداشته شده
	# مثلا آدرس آسیاتک توی tsetmc اینه: http://main.tsetmc.com/InstInfo/14079693677610396
	# اون تیکه آخرش میشه symbol_id
	symbol = Symbol(symbol_id='14079693677610396')
	
	# اطلاعات قیمتی داخل در یک نگاه
	price_overview = await symbol.aio_get_price_overview()
	print(f'price overview: \n\t', price_overview)

	# چارت داخل در یک نگاه
	intraday_price_chart_data = await symbol.aio_get_intraday_price_chart_data()
	print(f'interaday price chart data({len(intraday_price_chart_data)}):\n', '\n'.join(f'\t {item}' for item in intraday_price_chart_data[-5:]))

	# پیام ناظر
	supervisor_message_data = await symbol.aio_get_supervisor_messages_data()
	print(f'supervisor message data({len(supervisor_message_data)}):\n', '\n'.join(f'\t {item}' for item in supervisor_message_data[-5:]))

	# اطلاعیه
	notification_data = await symbol.aio_get_notifications_data()
	print(f'notification data({len(notification_data)}):\n', '\n'.join(f'\t {item}' for item in notification_data[-5:]))

	# تغییر وضعیت
	state_changes_data = await symbol.aio_get_state_changes_data()
	print(f'state changes data({len(state_changes_data)}):\n', '\n'.join(f'\t {item}' for item in state_changes_data[-5:]))

	# سابقه
	daily_history = await symbol.aio_get_daily_history()
	print(f'daily history data({len(daily_history)}):\n', '\n'.join(f'\t {item}' for item in daily_history[-5:]))

	# شناسه
	id_details = await symbol.aio_get_id_details()
	print(f'id details: \n\t', id_details)

	# حقیقی حقوقی
	traders_type_history = await symbol.aio_get_traders_type_history()
	print(f'traders type history({len(traders_type_history)}):\n', '\n'.join(f'\t {item}' for item in traders_type_history[-5:]))
	
	# سهامداران
	shareholders = await symbol.aio_get_shareholders_data()
	print(f'share holders({len(shareholders)}):\n', '\n'.join(f'\t {item}' for item in shareholders[-5:]))
	
	if shareholders:
		sh = shareholders[0]
		print(f'shareholder info: {sh.shareholder.name}')
	else:
		print('no shareholders found')
		return

	# چارتی که وقتی روی یک سهامدار کلیک میکنیم میده
	shareholder_chart_data = await sh.aio_get_chart_data()
	print(f'share holder chart data({len(shareholder_chart_data)}):\n', '\n'.join(f'\t {item}' for item in shareholder_chart_data[-5:]))

	# سایر سهام سهامدار عمده
	shareholder_portfolio_data = await sh.shareholder.aio_get_portfolio_data()
	print(f'share holder portfolio data({len(shareholder_portfolio_data)}):\n', '\n'.join(f'\t {item}' for item in shareholder_portfolio_data[-5:]))


if __name__ == '__main__':
	print('RunMode: Sync')
	method_sync()
	
	print('RunMode: Async')
	
	from asyncio import run

	run(method_async())
