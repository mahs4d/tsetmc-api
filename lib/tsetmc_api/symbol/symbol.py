from . import _core
from .group import SymbolGroupDataRow
from .identification import SymbolIdDetails
from .notification import SymbolNotificationsDataRow
from .orderbook import SymbolOrderBookData, SymbolOrderBookDataRow
from .price import SymbolPriceOverview, SymbolIntraDayPriceChartDataRow, SymbolPriceData, SymbolDailyPriceDataRow
from .shareholder import SymbolShareHolderDataRow, SymbolShareHolder
from .state_change import SymbolStateChangeDataRow
from .supervisor_message import SymbolSupervisorMessageDataRow
from .traders_type import SymbolTradersTypeDataRow, SymbolTradersTypeInfo, SymbolTradersTypeSubInfo


class Symbol:
    def __init__(self, symbol_id: str):
        self.symbol_id = symbol_id

    def get_price_overview(self) -> SymbolPriceOverview:
        """
        gets the last price overview of the symbol and returns most of the information (in "dar yek negah" tab)
        """

        raw_data = _core.get_symbol_price_overview(symbol_id=self.symbol_id)

        tick = SymbolPriceData(
            last=raw_data['price_data']['last'],
            close=raw_data['price_data']['close'],
            open=raw_data['price_data']['open'],
            yesterday=raw_data['price_data']['yesterday'],
            high=raw_data['price_data']['high'],
            low=raw_data['price_data']['low'],
            count=raw_data['price_data']['count'],
            volume=raw_data['price_data']['volume'],
            value=raw_data['price_data']['value'],
        )

        sell_rows = [SymbolOrderBookDataRow(
            count=row['count'],
            price=row['price'],
            volume=row['volume'],
        ) for row in raw_data['orderbook_data']['sell_rows']]
        buy_rows = [SymbolOrderBookDataRow(
            count=row['count'],
            price=row['price'],
            volume=row['volume'],
        ) for row in raw_data['orderbook_data']['buy_rows']]
        orderbook = SymbolOrderBookData(
            sell_rows=sell_rows,
            buy_rows=buy_rows,
        )

        traders_type = SymbolTradersTypeDataRow(
            legal=SymbolTradersTypeInfo(
                buy=SymbolTradersTypeSubInfo(
                    count=raw_data['traders_type_data']['legal']['buy']['count'],
                    volume=raw_data['traders_type_data']['legal']['buy']['volume'],
                    value=raw_data['traders_type_data']['legal']['buy']['value'],
                ),
                sell=SymbolTradersTypeSubInfo(
                    count=raw_data['traders_type_data']['legal']['sell']['count'],
                    volume=raw_data['traders_type_data']['legal']['sell']['volume'],
                    value=raw_data['traders_type_data']['legal']['sell']['value'],
                ),
            ),
            real=SymbolTradersTypeInfo(
                buy=SymbolTradersTypeSubInfo(
                    count=raw_data['traders_type_data']['real']['buy']['count'],
                    volume=raw_data['traders_type_data']['real']['buy']['volume'],
                    value=raw_data['traders_type_data']['real']['buy']['value'],
                ),
                sell=SymbolTradersTypeSubInfo(
                    count=raw_data['traders_type_data']['real']['sell']['count'],
                    volume=raw_data['traders_type_data']['real']['sell']['volume'],
                    value=raw_data['traders_type_data']['real']['sell']['value'],
                ),
            ),
        )

        group_data = [SymbolGroupDataRow(
            symbol_id=row['symbol_id'],
            last=row['last'],
            close=row['close'],
            count=row['count'],
            volume=row['volume'],
            value=row['value'],
        ) for row in raw_data['group_data']]

        return SymbolPriceOverview(
            price_data=tick,
            orderbook=orderbook,
            traders_type=traders_type,
            group_data=group_data,
        )

    def get_intraday_price_chart_data(self) -> list[SymbolIntraDayPriceChartDataRow]:
        """
        gets last days intraday price chart (in "dar yek negah" tab)
        """

        raw_data = _core.get_symbol_intraday_price_chart(symbol_id=self.symbol_id)

        ticks = [SymbolIntraDayPriceChartDataRow(
            time=row['time'],
            high=row['high'],
            low=row['low'],
            open=row['open'],
            close=row['close'],
            volume=row['volume'],
        ) for row in raw_data]

        return ticks

    def get_supervisor_messages_data(self) -> list[SymbolSupervisorMessageDataRow]:
        """
        get list of supervisor messages (in "payame nazer" tab)
        """

        raw_data = _core.get_symbol_supervisor_messages(symbol_id=self.symbol_id)

        messages = [SymbolSupervisorMessageDataRow(
            datetime=row['datetime'],
            title=row['title'],
            content=row['content'],
        ) for row in raw_data]

        return messages

    def get_notifications_data(self) -> list[SymbolNotificationsDataRow]:
        """
        get list of notifications (in "etelaiye ha" tab)
        """

        raw_data = _core.get_symbol_notifications(symbol_id=self.symbol_id)

        notifications = [SymbolNotificationsDataRow(
            datetime=row['datetime'],
            title=row['title'],
        ) for row in raw_data]

        return notifications

    def get_state_changes_data(self) -> list[SymbolStateChangeDataRow]:
        """
        get list of state changes (in "taghire vaziat" tab)
        """

        raw_data = _core.get_symbol_state_changes(symbol_id=self.symbol_id)

        state_changes = [SymbolStateChangeDataRow(
            datetime=row['datetime'],
            new_state=row['new_state'],
        ) for row in raw_data]

        return state_changes

    def get_daily_history(self) -> list[SymbolDailyPriceDataRow]:
        """
        get list of daily ticks history (in "sabeghe" tab)
        """

        raw_data = _core.get_symbol_daily_ticks_history(symbol_id=self.symbol_id)

        ticks = [SymbolDailyPriceDataRow(
            date=row['date'],
            last=row['last'],
            close=row['close'],
            open=row['open'],
            yesterday=row['yesterday'],
            high=row['high'],
            low=row['low'],
            count=row['count'],
            volume=row['volume'],
            value=row['value'],
        ) for row in raw_data]

        return ticks

    def get_id_details(self) -> SymbolIdDetails:
        """
        gets symbol identity details and returns all the information (in "shenase" tab)
        """

        raw_data = _core.get_symbol_id_details(symbol_id=self.symbol_id)

        details = SymbolIdDetails(
            isin=raw_data['isin'],
            short_isin=raw_data['short_isin'],
            short_name=raw_data['short_name'],
            long_name=raw_data['long_name'],
            english_name=raw_data['english_name'],

            company_isin=raw_data['company_isin'],
            company_short_isin=raw_data['company_short_isin'],
            company_name=raw_data['company_name'],

            market_code=raw_data['market_code'],
            market_name=raw_data['market_name'],

            group_code=raw_data['group_code'],
            group_name=raw_data['group_name'],

            subgroup_code=raw_data['subgroup_code'],
            subgroup_name=raw_data['subgroup_name'],
        )

        return details

    def get_traders_type_history(self) -> list[SymbolTradersTypeDataRow]:
        """
        returns daily traders type history (in "haghihi-hoghooghi" tab)
        """

        raw_data = _core.get_symbol_traders_type_history(symbol_id=self.symbol_id)

        traders_type_history = [SymbolTradersTypeDataRow(
            legal=SymbolTradersTypeInfo(
                buy=SymbolTradersTypeSubInfo(
                    count=row['legal']['buy']['count'],
                    volume=row['legal']['buy']['volume'],
                    value=row['legal']['buy']['value'],
                ),
                sell=SymbolTradersTypeSubInfo(
                    count=row['legal']['sell']['count'],
                    volume=row['legal']['sell']['volume'],
                    value=row['legal']['sell']['value'],
                ),
            ),
            real=SymbolTradersTypeInfo(
                buy=SymbolTradersTypeSubInfo(
                    count=row['real']['buy']['count'],
                    volume=row['real']['buy']['volume'],
                    value=row['real']['buy']['value'],
                ),
                sell=SymbolTradersTypeSubInfo(
                    count=row['real']['sell']['count'],
                    volume=row['real']['sell']['volume'],
                    value=row['real']['sell']['value'],
                ),
            ),
        ) for row in raw_data]

        return traders_type_history

    def get_shareholders_data(self) -> list[SymbolShareHolderDataRow]:
        """
        returns list of major shareholders (in "saham daran" tab)
        """

        company_isin = self.get_id_details().company_isin
        raw_data = _core.get_symbol_shareholders(company_isin=company_isin)

        shareholders = [SymbolShareHolderDataRow(
            shareholder=SymbolShareHolder(
                _company_isin=company_isin,
                id=row['id'],
                name=row['name'],
            ),
            count=row['count'],
            percentage=row['percentage'],
            change=row['change'],
        ) for row in raw_data]

        return shareholders
