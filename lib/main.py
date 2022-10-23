from jdatetime import date as jdate

from tsetmc_api_new.day_details import DayDetails

SYMBOL_ID = '3839324986781871'
DATE = jdate(1401, 7, 25)

details = DayDetails(symbol_id=SYMBOL_ID, date=DATE)

# output1 = details.get_price_overview()
# output2 = details.get_price_data()
# output3 = details.get_orderbook_data()
# output4 = details.get_trade_data()
output5 = details.get_traders_type_data()
print(output5)