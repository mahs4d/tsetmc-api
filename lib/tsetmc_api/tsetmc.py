import pprint

from day_details import AssetDayDetails

vbmellat_20200704 = AssetDayDetails('778253364357513', 2020, 7, 4)
# print(vbmellat_20200704.get_asset_details())
# print(vbmellat_20200704.get_yesterday_close_price())
# print(vbmellat_20200704.get_trades())
# print(vbmellat_20200704.get_shareholders())
# print(vbmellat_20200704.get_yesterday_shareholders())
pp = pprint.PrettyPrinter(indent=4, depth=5)
pp.pprint(vbmellat_20200704.get_tick_at(10, 14, 41))
