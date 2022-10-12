from abc import ABC, abstractmethod

from .watch_tick import MarketWatchTick


class Filter(ABC):
    @abstractmethod
    def filter(self, symbol_id: str, watch_tick: MarketWatchTick) -> bool:
        pass
