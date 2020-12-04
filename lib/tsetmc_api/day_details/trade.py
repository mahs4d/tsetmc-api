from __future__ import annotations

from dataclasses import dataclass
from time import time
from typing import List, Dict

from tsetmc_api.utils import int_to_time


@dataclass
class Trade:
    time: time
    order: int
    price: int
    volume: int

    @staticmethod
    def from_raw_trades_data(raw_trades_data: List[Dict]) -> List[Trade]:
        return [Trade(
            time=int_to_time(x['t']),
            order=x['order'],
            price=x['p'],
            volume=x['v'],
        ) for x in raw_trades_data]
