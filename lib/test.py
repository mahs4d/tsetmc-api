from tsetmc_api.symbol import Symbol

a = Symbol('22560050433388046')
b = a.get_daily_history()
c = a.get_day_details(1399, 9, 5)
d = a.get_details()
e = a.get_major_shareholders()
