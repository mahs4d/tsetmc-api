from __future__ import annotations

from dataclasses import dataclass
from datetime import time
from typing import List, Dict

from tsetmc_api.types import Price
from tsetmc_api.utils import int_to_time


@dataclass
class SnapshotOrder:
    time: time
    price: Price
    count: int
    volume: int


@dataclass
class Snapshot:
    time: time
    open: Price
    close: Price
    last: Price
    high: Price
    low: Price
    yesterday: Price
    count: int
    volume: int
    state: str
    buy_orders: List[SnapshotOrder]
    sell_orders: List[SnapshotOrder]

    @staticmethod
    def from_raw_day_details(price_data: Dict, orders_data: List[Dict]) -> Snapshot:
        max_t = price_data['t']
        snapshot = Snapshot(
            time=int_to_time(max_t),
            last=price_data['lst'],
            yesterday=price_data['y'],
            open=price_data['o'],
            high=price_data['h'],
            close=price_data['c'],
            low=price_data['l'],
            count=price_data['cnt'],
            volume=price_data['v'],
            state=price_data['s'],
            buy_orders=[],
            sell_orders=[]
        )

        for to in orders_data:
            if to is not None:
                snapshot.buy_orders.append(SnapshotOrder(
                    time=int_to_time(to['t']),
                    count=to['bcnt'],
                    volume=to['bv'],
                    price=to['bp'],
                ))
                snapshot.sell_orders.append(SnapshotOrder(
                    time=int_to_time(to['t']),
                    count=to['scnt'],
                    volume=to['sv'],
                    price=to['sp'],
                ))

                max_t = max(max_t, to['t'])

        snapshot.time = int_to_time(max_t)

        return snapshot

    @staticmethod
    def generate_snapshots_from_raw_day_detail_data(price_data: List[Dict], orders_data: List[Dict]) -> Iterator[
        Snapshot]:
        max_pdi = len(price_data)
        max_odi = len(orders_data)
        pdi = 0
        odi = -1
        last_price_data = price_data[pdi]
        last_orders_data = [None, None, None]

        while True:
            phase = -1
            if pdi + 1 < max_pdi and odi + 1 < max_odi:
                if price_data[pdi + 1]['t'] < orders_data[odi + 1]['t']:
                    phase = 1
                elif price_data[pdi + 1]['t'] > orders_data[odi + 1]['t']:
                    phase = 2
                else:
                    phase = 3
            else:
                if pdi + 1 == max_pdi and odi + 1 == max_odi:
                    break
                elif pdi + 1 < max_pdi:
                    phase = 1
                elif odi + 1 < max_odi:
                    phase = 2

            # step price data and use the old order data
            if phase == 1 or phase == 3:
                pdi += 1
                last_price_data = price_data[pdi]

            # step orders
            if phase == 2 or phase == 3:
                t = orders_data[odi + 1]['t']
                orders_found = [None, None, None]
                while True:
                    if odi + 1 >= max_odi:
                        break

                    order = orders_data[odi + 1]
                    rank = min(order['rank'] - 1, 2)
                    if orders_found[rank] is not None or order['t'] > t:
                        break

                    odi += 1
                    orders_found[rank] = order
                    last_orders_data[rank] = order

            yield Snapshot.from_raw_day_details(last_price_data, last_orders_data)
