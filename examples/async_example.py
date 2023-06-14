import asyncio

from tsetmc_api.symbol import Symbol


async def main():
    # دیدن مشخصات یک نماد (نماد آسیاتک)
    # این عددی که به عنوان symbol_id بهش میدیم، از تیکه‌ی آخر url صفحه‌ی آسیاتک توی سایت برداشته شده
    # مثلا آدرس آسیاتک توی tsetmc اینه: http://main.tsetmc.com/InstInfo/14079693677610396
    # اون تیکه آخرش میشه symbol_id
    symbol = Symbol(symbol_id='14079693677610396')

    # اطلاعات قیمتی داخل در یک نگاه
    # نام تابع دقیقا همان نام تابع sync است با یک پسوند _async
    price_overview = await symbol.get_price_overview_async()
    print(price_overview)


if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())
