from tsetmc_api.symbol import Symbol

# دیدن مشخصات یک نماد (نماد آسیاتک)
# این عددی که به عنوان symbol_id بهش میدیم، از تیکه‌ی آخر url صفحه‌ی آسیاتک توی سایت برداشته شده
# مثلا آدرس آسیاتک توی tsetmc اینه: http://main.tsetmc.com/InstInfo/14079693677610396
# اون تیکه آخرش میشه symbol_id
symbol = Symbol(symbol_id='14079693677610396')

# اطلاعات قیمتی داخل در یک نگاه
price_overview = symbol.get_price_overview()

# چارت داخل در یک نگاه
intraday_price_chart_data = symbol.get_intraday_price_chart_data()

# پیام ناظر
supervisor_message_data = symbol.get_supervisor_messages_data()

# اطلاعیه
notification_data = symbol.get_notifications_data()

# تغییر وضعیت
state_changes_data = symbol.get_state_changes_data()

# سابقه
daily_history = symbol.get_daily_history()

# شناسه
id_details = symbol.get_id_details()

# حقیقی حقوقی
traders_type_history = symbol.get_traders_type_history()

# سهامداران
shareholders = symbol.get_shareholders_data()

# چارتی که وقتی روی یک سهامدار کلیک میکنیم میده
shareholder_chart_data = shareholders[0].get_chart_data()

# سایر سهام سهامدار عمده
shareholder_portfolio_data = shareholders[0].shareholder.get_portfolio_data()
