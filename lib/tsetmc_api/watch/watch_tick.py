from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Dict, List, Union

from tsetmc_api.types import SymbolId, Price


@dataclass
class SymbolOrderData:
    rank: int
    count: int
    price: Price
    volume: int

    @staticmethod
    def from_dict(dictionary: Union[Dict, List]) -> Union[SymbolOrderData, List[SymbolOrderData]]:
        if dictionary is None:
            return []

        if type(dictionary) == list:
            return [SymbolOrderData.from_dict(d) for d in dictionary]

        return SymbolOrderData(
            rank=dictionary.get('rank'),
            count=dictionary.get('count'),
            price=dictionary.get('price'),
            volume=dictionary.get('volume'),
        )


@dataclass
class SymbolPriceData:
    symbol_short_name: str
    symbol_long_name: str
    isin: str
    heven: int
    open: Price
    close: Price
    last: Price
    high: Price
    low: Price
    count: int
    volume: int
    value: int
    yesterday: Price
    eps: Optional[int]
    base_volume: int
    visits_count: int
    flow: int
    group_code: int
    max: Price
    min: Price
    z: int
    yval: int
    buy_orders: List[SymbolOrderData]
    sell_orders: List[SymbolOrderData]

    @staticmethod
    def from_dict(dictionary: Union[Dict, List]) -> Union[SymbolPriceData, List[SymbolPriceData]]:
        if type(dictionary) == list:
            return [SymbolPriceData.from_dict(d) for d in dictionary]

        return SymbolPriceData(
            symbol_short_name=dictionary.get('symbol_short_name'),
            symbol_long_name=dictionary.get('symbol_long_name'),
            isin=dictionary.get('isin'),
            heven=dictionary.get('heven'),
            open=dictionary.get('open'),
            close=dictionary.get('close'),
            last=dictionary.get('last'),
            high=dictionary.get('high'),
            low=dictionary.get('low'),
            count=dictionary.get('count'),
            volume=dictionary.get('volume'),
            value=dictionary.get('value'),
            yesterday=dictionary.get('yesterday'),
            eps=dictionary.get('eps'),
            base_volume=dictionary.get('base_volume'),
            visits_count=dictionary.get('visits_count'),
            flow=dictionary.get('flow'),
            group_code=dictionary.get('group_code'),
            max=dictionary.get('max'),
            min=dictionary.get('min'),
            z=dictionary.get('z'),
            yval=dictionary.get('yval'),
            buy_orders=SymbolOrderData.from_dict(dictionary.get('buy_orders')),
            sell_orders=SymbolOrderData.from_dict(dictionary.get('sell_orders')),
        )


@dataclass
class SymbolClientTypeDataDetails:
    buy_count: int
    buy_volume: int
    sell_count: int
    sell_volume: int

    @staticmethod
    def from_dict(dictionary: Union[Dict, List]) -> Union[
        SymbolClientTypeDataDetails, List[SymbolClientTypeDataDetails]]:
        if type(dictionary) == list:
            return [SymbolClientTypeDataDetails.from_dict(d) for d in dictionary]

        return SymbolClientTypeDataDetails(
            buy_count=dictionary.get('buy_count'),
            buy_volume=dictionary.get('buy_volume'),
            sell_count=dictionary.get('sell_count'),
            sell_volume=dictionary.get('sell_volume'),
        )


@dataclass
class SymbolClientTypeData:
    legal: SymbolClientTypeDataDetails
    individual: SymbolClientTypeDataDetails

    @staticmethod
    def from_dict(dictionary: Union[Dict, List]) -> Union[SymbolClientTypeData, List[SymbolClientTypeData]]:
        if type(dictionary) == list:
            return [SymbolClientTypeData.from_dict(d) for d in dictionary]

        return SymbolClientTypeData(
            legal=SymbolClientTypeDataDetails.from_dict(dictionary.get('legal')),
            individual=SymbolClientTypeDataDetails.from_dict(dictionary.get('individual')),
        )


@dataclass
class SymbolHistoricalDayData:
    open: Price
    close: Price
    last: Price
    high: Price
    low: Price
    count: int
    volume: int
    value: int
    yesterday: Price

    @staticmethod
    def from_dict(dictionary: Union[Dict, List]) -> Union[SymbolHistoricalDayData, List[SymbolHistoricalDayData]]:
        if type(dictionary) == list:
            return [SymbolHistoricalDayData.from_dict(d) for d in dictionary]

        return SymbolHistoricalDayData(
            open=dictionary.get('open'),
            close=dictionary.get('close'),
            last=dictionary.get('last'),
            high=dictionary.get('high'),
            low=dictionary.get('low'),
            count=dictionary.get('count'),
            volume=dictionary.get('volume'),
            value=dictionary.get('value'),
            yesterday=dictionary.get('yesterday'),
        )


@dataclass
class SymbolStatsData:
    pass


@dataclass
class WatchTick:
    price_data: Optional[Dict[SymbolId, SymbolPriceData]]
    client_type_data: Optional[Dict[SymbolId, SymbolClientTypeData]]
    historical_data: Optional[Dict[SymbolId, List[SymbolHistoricalDayData]]]
    stats_data: Optional[Dict[SymbolId, SymbolStatsData]]

    def __init__(self,
                 price_data: Optional[Dict[SymbolId, SymbolPriceData]],
                 client_type_data: Optional[Dict[SymbolId, SymbolClientTypeData]],
                 historical_data: Optional[Dict[SymbolId, List[SymbolHistoricalDayData]]],
                 stats_data: Optional[Dict[SymbolId, SymbolStatsData]]):
        self.price_data = price_data
        self.client_type_data = client_type_data
        self.historical_data = historical_data
        self.stats_data = stats_data

    def get_symbol_ids(self) -> List[SymbolId]:
        """
        لیست آی دی همه‌ی نمادهای داخل دیده‌بان
        """
        if self.price_data is not None:
            return list(self.price_data.keys())
        elif self.client_type_data is not None:
            return list(self.client_type_data.keys())
        elif self.historical_data is not None:
            return list(self.historical_data.keys())
        elif self.stats_data is not None:
            return list(self.stats_data.keys())

    def get_price_data(self, symbol_id) -> Optional[SymbolPriceData]:
        """
        اطلاعات قیمتی و سفارشات دیده‌بان
        """
        if self.price_data is None:
            return None

        return self.price_data.get(symbol_id)

    def get_client_type_data(self, symbol_id) -> Optional[SymbolClientTypeData]:
        """
        اطلاعات حقیقی حقوقی دیده‌بان
        """
        if self.client_type_data is None:
            return None

        return self.client_type_data.get(symbol_id)

    def get_historical_data(self, symbol_id) -> Optional[dict]:
        """
        اطلاعات سابقه‌ی دیده‌بان
        """
        if self.historical_data is None:
            return None

        return self.historical_data.get(symbol_id)

    def get_stats_data(self, symbol_id) -> Optional[SymbolStatsData]:
        """
        آمارهای کلیدی دیده‌بان
        """
        if self.stats_data is None:
            return None

        return self.stats_data.get(symbol_id)
