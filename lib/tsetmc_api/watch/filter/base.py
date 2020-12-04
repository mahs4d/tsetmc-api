from abc import ABC, abstractmethod

from tsetmc_api.types import SymbolId
from ..watch_tick import WatchTick


class Filter(ABC):
    @abstractmethod
    def apply(self, symbol_id: SymbolId, watch_tick: WatchTick) -> bool:
        raise NotImplementedError('apply method of filter should be implemented')

    def get_filtered_tick(self, watch_tick: WatchTick) -> WatchTick:
        price_data = None
        historical_data = None
        stats_data = None
        client_type_data = None

        for symbol_id in watch_tick.get_symbol_ids():
            if self.apply(symbol_id, watch_tick):
                symbol_price_data = watch_tick.get_price_data(symbol_id)
                symbol_client_type_data = watch_tick.get_client_type_data(symbol_id)
                symbol_historical_data = watch_tick.get_historical_data(symbol_id)
                symbol_stats_data = watch_tick.get_stats_data(symbol_id)

                if symbol_price_data is not None:
                    if price_data is None:
                        price_data = {}
                    price_data[symbol_id] = symbol_price_data

                if symbol_client_type_data is not None:
                    if client_type_data is None:
                        client_type_data = {}
                    client_type_data[symbol_id] = symbol_client_type_data

                if symbol_historical_data is not None:
                    if historical_data is None:
                        historical_data = {}
                    historical_data[symbol_id] = symbol_historical_data

                if symbol_stats_data is not None:
                    if stats_data is None:
                        stats_data = {}
                    stats_data[symbol_id] = symbol_stats_data

        return WatchTick(price_data=price_data,
                         client_type_data=client_type_data,
                         historical_data=historical_data,
                         stats_data=stats_data)

    def __and__(self, other):
        me = self

        class AndFilter(Filter):
            def apply(self, symbol_id: str, watch_tick: WatchTick):
                return me.apply(symbol_id, watch_tick) and other.apply(symbol_id, watch_tick)

        return AndFilter()

    def __or__(self, other):
        me = self

        class OrFilter(Filter):
            def apply(self, symbol_id: str, watch_tick: WatchTick):
                return me.apply(symbol_id, watch_tick) or other.apply(symbol_id, watch_tick)

        return OrFilter()

    def __invert__(self):
        me = self

        class InvertedFilter(Filter):
            def apply(self, symbol_id: str, watch_tick: WatchTick):
                return not me.apply(symbol_id, watch_tick)

        return InvertedFilter()
