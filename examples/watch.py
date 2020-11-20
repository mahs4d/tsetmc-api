"""
در این مثال یک فیلتر ورود پول هوشمند رو روی دیده‌بان اجرا میکنیم و لیست نمادها رو چاپ میکنیم

فیلتری که اعمال میکنیم به این شکله که تمام نمادهایی که سرانه خریدار حقیقی بالای ۴۰ میلیونه رو میخوایم چاپ کنه
"""

from tsetmc_api import Watch, Filter
from tsetmc_api.watch import WatchTick


class PooleHooshmandFilter(Filter):
    def apply(self, asset_id, watch_tick: WatchTick):
        client_type_data = watch_tick.get_client_type_data(asset_id)  # گرفتن اطلاعات حقیقی حقوقی سهم

        # بعضی از سهما اطلاعات حقیقی حقوقی ندارند (نمیدونم چرا) اونارو میندازیم بیرون
        if client_type_data == {}:
            return False

        natural_ct_data = client_type_data.get('natural', None)  # بخش حقیقیش

        buy_volume = natural_ct_data.get('buy_volume')  # حجم خرید حقیقی
        buy_count = natural_ct_data.get('buy_count')  # تعداد خریدار حقیقی
        close = watch_tick.get_simple_data(asset_id).get('close')  # قیمت نهایی سهم

        # برای جلوگیری از تقسیم بر صفر
        if buy_count == 0:
            return False

        sarane_kharidar = (buy_volume / buy_count) * close

        if sarane_kharidar >= 400000000:
            return True
        
        return False


def on_poolehooshmand_tick(tick: WatchTick):
    print('-----------------------------------------------------------------')

    asset_ids = tick.get_symbol_ids()
    for asset_id in asset_ids:
        print(tick.get_simple_data(asset_id)['symbol_short_name'])

    print('-----------------------------------------------------------------')


if __name__ == '__main__':
    # declare our Watch
    watch = Watch()

    # now we tell watch to call our listener function with output of PooleHooshmandFilter for each tick
    watch.bind_listener(on_poolehooshmand_tick, PooleHooshmandFilter())

    # start the watch
    watch.start_watch()
