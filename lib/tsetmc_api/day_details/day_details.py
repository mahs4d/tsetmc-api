from jdatetime import date as jdate

from . import _core
from .orderbook import DayDetailsOrderBookDataRow, DayDetailsOrderBookRow
from .price import DayDetailsPriceDataRow, DayDetailsPriceOverview
from .shareholder import DayDetailsShareHolderDataRow, DayDetailsShareHolder
from .threshold import DayDetailsThresholdsData
from .trade import DayDetailsTradeDataRow
from .traders_type import DayDetailsTradersTypeData, DayDetailsTradersTypeInfo, DayDetailsTradersTypeSubInfo


class DayDetails:
    def __init__(self, symbol_id: str, date: jdate):
        self.symbol_id = symbol_id
        self.date = date

    def get_price_overview(self) -> DayDetailsPriceOverview:
        """
        returns an overview of price information for that day
        """

        raw_data = _core.get_day_details_price_overview(symbol_id=self.symbol_id, date=self.date)

        return DayDetailsPriceOverview(
            price_change=raw_data['price_change'],
            low=raw_data['low'],
            high=raw_data['high'],
            yesterday=raw_data['yesterday'],
            open=raw_data['open'],
            close=raw_data['close'],
            last=raw_data['last'],
            count=raw_data['count'],
            volume=raw_data['volume'],
            value=raw_data['value'],
        )

    def get_price_data(self) -> list[DayDetailsPriceDataRow]:
        """
        returns instant prices (for each time in that date)
        """

        raw_data = _core.get_day_details_price_data(symbol_id=self.symbol_id, date=self.date)

        return [DayDetailsPriceDataRow(
            time=row['time'],
            close=row['close'],
            last=row['last'],
            value=row['value'],
            volume=row['volume'],
            count=row['count'],
        ) for row in raw_data]

    def get_orderbook_data(self) -> list[DayDetailsOrderBookDataRow]:
        """
        returns instant orderbooks (for each time in that date)
        """

        raw_data = _core.get_day_details_orderbook_data(symbol_id=self.symbol_id, date=self.date)

        return [DayDetailsOrderBookDataRow(
            time=data['time'],
            buy_rows=[DayDetailsOrderBookRow(
                time=row['time'],
                count=row['count'],
                price=row['price'],
                volume=row['volume'],
            ) for row in data['buy_rows']],
            sell_rows=[DayDetailsOrderBookRow(
                time=row['time'],
                count=row['count'],
                price=row['price'],
                volume=row['volume'],
            ) for row in data['sell_rows']],
        ) for data in raw_data]

    def get_traders_type_data(self) -> DayDetailsTradersTypeData:
        """
        returns traders type information for that day
        """

        raw_data = _core.get_day_details_traders_type_data(symbol_id=self.symbol_id, date=self.date)

        return DayDetailsTradersTypeData(
            legal=DayDetailsTradersTypeInfo(
                buy=DayDetailsTradersTypeSubInfo(
                    count=raw_data['legal']['buy']['count'],
                    volume=raw_data['legal']['buy']['volume'],
                    value=raw_data['legal']['buy']['value'],
                ),
                sell=DayDetailsTradersTypeSubInfo(
                    count=raw_data['legal']['sell']['count'],
                    volume=raw_data['legal']['sell']['volume'],
                    value=raw_data['legal']['sell']['value'],
                ),
            ),
            real=DayDetailsTradersTypeInfo(
                buy=DayDetailsTradersTypeSubInfo(
                    count=raw_data['real']['buy']['count'],
                    volume=raw_data['real']['buy']['volume'],
                    value=raw_data['real']['buy']['value'],
                ),
                sell=DayDetailsTradersTypeSubInfo(
                    count=raw_data['real']['sell']['count'],
                    volume=raw_data['real']['sell']['volume'],
                    value=raw_data['real']['sell']['value'],
                ),
            ),
        )

    def get_trades_data(self, summarize: bool = False) -> list[DayDetailsTradeDataRow]:
        """
        gets all trade data
        """

        raw_data = _core.get_day_details_trade_data(symbol_id=self.symbol_id, date=self.date, summarize=summarize)

        return [DayDetailsTradeDataRow(
            time=row['time'],
            price=row['price'],
            volume=row['volume'],
        ) for row in raw_data]

    def get_thresholds_data(self) -> DayDetailsThresholdsData:
        raw_data = _core.get_day_details_thresholds_data(symbol_id=self.symbol_id, date=self.date)
        return DayDetailsThresholdsData(
            range_max=raw_data['max'],
            range_min=raw_data['min'],
        )

    def get_shareholders_data(self) -> tuple[list[DayDetailsShareHolderDataRow], list[DayDetailsShareHolderDataRow]]:
        """
        gets list of shareholders before and after the day
        """

        raw_old_shareholders, raw_new_shareholders = _core.get_day_details_shareholders_data(
            symbol_id=self.symbol_id,
            date=self.date,
        )

        old_shareholders = [DayDetailsShareHolderDataRow(
            shareholder=DayDetailsShareHolder(id=row['id'], name=row['name']),
            count=row['count'],
            percentage=row['percentage'],
        ) for row in raw_old_shareholders]

        new_shareholders = [DayDetailsShareHolderDataRow(
            shareholder=DayDetailsShareHolder(id=row['id'], name=row['name']),
            count=row['count'],
            percentage=row['percentage'],
        ) for row in raw_new_shareholders]

        return old_shareholders, new_shareholders
