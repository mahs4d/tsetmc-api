from .base import Filter
from ..watch_tick import WatchTick


class SahamFilter(Filter):
    def apply(self, symbol_id: str, watch_tick: WatchTick) -> bool:
        price_data = watch_tick.get_price_data(symbol_id=symbol_id)
        if price_data is None:
            return False

        yval = price_data.yval
        return yval in [300, 303, 313]


class PayeFarabourseFilter(Filter):
    def apply(self, symbol_id: str, watch_tick: WatchTick) -> bool:
        price_data = watch_tick.get_price_data(symbol_id=symbol_id)
        if price_data is None:
            return False

        yval = price_data.yval
        return yval in [309]


class HaghTaghaddomFilter(Filter):
    def apply(self, symbol_id: str, watch_tick: WatchTick) -> bool:
        price_data = watch_tick.get_price_data(symbol_id=symbol_id)
        if price_data is None:
            return False

        yval = price_data.yval
        return yval in [400, 403, 404]


class OraghMosharekatFilter(Filter):
    def apply(self, symbol_id: str, watch_tick: WatchTick) -> bool:
        price_data = watch_tick.get_price_data(symbol_id=symbol_id)
        if price_data is None:
            return False

        yval = price_data.yval
        return yval in [306, 301, 706, 208]


class AtiFilter(Filter):
    def apply(self, symbol_id: str, watch_tick: WatchTick) -> bool:
        price_data = watch_tick.get_price_data(symbol_id=symbol_id)
        if price_data is None:
            return False

        yval = price_data.yval
        return yval in [263]


class SandoghFilter(Filter):
    def apply(self, symbol_id: str, watch_tick: WatchTick) -> bool:
        price_data = watch_tick.get_price_data(symbol_id=symbol_id)
        if price_data is None:
            return False

        yval = price_data.yval
        return yval in [305, 380]


class EkhtiarForoushFilter(Filter):
    def apply(self, symbol_id: str, watch_tick: WatchTick) -> bool:
        price_data = watch_tick.get_price_data(symbol_id=symbol_id)
        if price_data is None:
            return False

        yval = price_data.yval
        return yval in [600, 602, 605, 311, 312]


class KalaForoushFilter(Filter):
    def apply(self, symbol_id: str, watch_tick: WatchTick) -> bool:
        price_data = watch_tick.get_price_data(symbol_id=symbol_id)
        if price_data is None:
            return False

        yval = price_data.yval
        return yval in [308, 701]
