from jdatetime import date as jdate

from tsetmc_api.day_details import DayDetails

# تغییرات نماد در یک روز
day_details = DayDetails(symbol_id='14079693677610396', date=jdate(1402, 3, 1))

# قیمت‌های نهایی
price_overview = day_details.get_price_overview()

# تغییرات قیمتی
price_data = day_details.get_price_data()

# تغییرات صف‌های خرید و فروش
orderbook_data = day_details.get_orderbook_data()

# معاملات
trades_data = day_details.get_trades_data()

# بیشترین و کمترین قیمت روز
thresholds_data = day_details.get_thresholds_data()

# تغییرات سهامداران عمده
old_shareholders, new_shareholders = day_details.get_shareholders_data()

# چارت یک سهامدار
old_shareholders[0].get_chart_data()

# سهام یک سهامدار عمده
old_shareholders[0].shareholder.get_portfolio_data()
