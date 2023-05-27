from tsetmc_api.market_watch import MarketWatch

# دیده‌بان بازار
# توجه کنید که این اطلاعات از صفحه‌ی دیده‌بان بازاره و مثلا سابقه‌ی اینجا با اون سابقه‌ای که توی صفحه
# نماد می‌بینیم فرق داره. اونا توی پکیج symbol قرار دارند.
market_watch = MarketWatch()

# اطلاعات قیمتی
price_data = market_watch.get_price_data()

# اطلاعات آماری به صورت خام
raw_stats_data = market_watch.get_raw_stats_data()

# اطلاعات آماری به صورت parse شده
stats_data = market_watch.get_stats_data()

# اطلاعات حقیقی حقوقی
traders_type_data = market_watch.get_traders_type_data()

# اطلاعات سابقه
daily_history_data = market_watch.get_daily_history_data()
