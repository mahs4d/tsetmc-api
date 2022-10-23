from . import _core
from .group import GroupDataRow
from .identification import SymbolIdDetails
from .notification import Notification
from .orderbook import OrderBook, OrderBookRow
from .price import SymbolPriceOverview, SymbolIntraDayPriceChartTick
from .shareholder import SymbolShareHolderRow, ShareHolder
from .state_change import StateChange
from .supervisor_message import SupervisorMessage
from .tick import Tick, DailyTick
from .traders_type import TradersTypeRow, TradersTypeData, TradersTypeSubData


class Symbol:
    def __init__(self, symbol_id: str):
        self.symbol_id = symbol_id

    def get_price_overview(self) -> SymbolPriceOverview:
        """
        gets the last price overview of the symbol and returns most of the information (in "dar yek negah" tab)
        """

        raw_data = _core.get_symbol_price_overview(symbol_id=self.symbol_id)

        tick = Tick(
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

        sell_rows = [OrderBookRow(
            count=row['count'],
            price=row['price'],
            volume=row['volume'],
        ) for row in raw_data['orderbook_data']['sell_rows']]
        buy_rows = [OrderBookRow(
            count=row['count'],
            price=row['price'],
            volume=row['volume'],
        ) for row in raw_data['orderbook_data']['buy_rows']]
        orderbook = OrderBook(
            sell_rows=sell_rows,
            buy_rows=buy_rows,
        )

        traders_type = TradersTypeRow(
            legal=TradersTypeData(
                buy=TradersTypeSubData(
                    count=raw_data['traders_type_data']['legal']['buy']['count'],
                    volume=raw_data['traders_type_data']['legal']['buy']['volume'],
                    value=raw_data['traders_type_data']['legal']['buy']['value'],
                ),
                sell=TradersTypeSubData(
                    count=raw_data['traders_type_data']['legal']['sell']['count'],
                    volume=raw_data['traders_type_data']['legal']['sell']['volume'],
                    value=raw_data['traders_type_data']['legal']['sell']['value'],
                ),
            ),
            real=TradersTypeData(
                buy=TradersTypeSubData(
                    count=raw_data['traders_type_data']['real']['buy']['count'],
                    volume=raw_data['traders_type_data']['real']['buy']['volume'],
                    value=raw_data['traders_type_data']['real']['buy']['value'],
                ),
                sell=TradersTypeSubData(
                    count=raw_data['traders_type_data']['real']['sell']['count'],
                    volume=raw_data['traders_type_data']['real']['sell']['volume'],
                    value=raw_data['traders_type_data']['real']['sell']['value'],
                ),
            ),
        )

        group_data = [GroupDataRow(
            symbol_id=row['symbol_id'],
            last=row['last'],
            close=row['close'],
            count=row['count'],
            volume=row['volume'],
            value=row['value'],
        ) for row in raw_data['group_data']]

        return SymbolPriceOverview(
            tick=tick,
            orderbook=orderbook,
            traders_type=traders_type,
            group_data=group_data,
        )

    def get_intraday_price_chart_ticks(self) -> list[SymbolIntraDayPriceChartTick]:
        """
        gets last days intraday price chart (in "dar yek negah" tab)
        """

        raw_data = _core.get_symbol_intraday_price_chart(symbol_id=self.symbol_id)

        ticks = [SymbolIntraDayPriceChartTick(
            time=row['time'],
            high=row['high'],
            low=row['low'],
            open=row['open'],
            close=row['close'],
            volume=row['volume'],
        ) for row in raw_data]

        return ticks

    def get_supervisor_messages(self) -> list[SupervisorMessage]:
        """
        get list of supervisor messages (in "payame nazer" tab)
        """

        raw_data = _core.get_symbol_supervisor_messages(symbol_id=self.symbol_id)

        messages = [SupervisorMessage(
            datetime=row['datetime'],
            title=row['title'],
            content=row['content'],
        ) for row in raw_data]

        return messages

    def get_notifications(self) -> list[Notification]:
        """
        get list of notifications (in "etelaiye ha" tab)
        """

        raw_data = _core.get_symbol_notifications(symbol_id=self.symbol_id)

        notifications = [Notification(
            datetime=row['datetime'],
            title=row['title'],
        ) for row in raw_data]

        return notifications

    def get_state_changes(self) -> list[StateChange]:
        """
        get list of state changes (in "taghire vaziat" tab)
        """

        raw_data = _core.get_symbol_state_changes(symbol_id=self.symbol_id)

        state_changes = [StateChange(
            datetime=row['datetime'],
            new_state=row['new_state'],
        ) for row in raw_data]

        return state_changes

    def get_daily_ticks_history(self) -> list[DailyTick]:
        """
        get list of daily ticks history (in "sabeghe" tab)
        """

        raw_data = _core.get_symbol_daily_ticks_history(symbol_id=self.symbol_id)

        ticks = [DailyTick(
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

    def get_traders_type_history(self) -> list[TradersTypeRow]:
        """
        returns daily traders type history (in "haghihi-hoghooghi" tab)
        """

        raw_data = _core.get_symbol_traders_type_history(symbol_id=self.symbol_id)

        traders_type_history = [TradersTypeRow(
            legal=TradersTypeData(
                buy=TradersTypeSubData(
                    count=row['legal']['buy']['count'],
                    volume=row['legal']['buy']['volume'],
                    value=row['legal']['buy']['value'],
                ),
                sell=TradersTypeSubData(
                    count=row['legal']['sell']['count'],
                    volume=row['legal']['sell']['volume'],
                    value=row['legal']['sell']['value'],
                ),
            ),
            real=TradersTypeData(
                buy=TradersTypeSubData(
                    count=row['real']['buy']['count'],
                    volume=row['real']['buy']['volume'],
                    value=row['real']['buy']['value'],
                ),
                sell=TradersTypeSubData(
                    count=row['real']['sell']['count'],
                    volume=row['real']['sell']['volume'],
                    value=row['real']['sell']['value'],
                ),
            ),
        ) for row in raw_data]

        return traders_type_history

    def get_major_shareholders(self) -> list[SymbolShareHolderRow]:
        """
        returns list of major shareholders (in "saham daran" tab)
        """

        raw_data = _core.get_symbol_major_shareholders(symbol_id=self.symbol_id)

        shareholders = [SymbolShareHolderRow(
            shareholder=ShareHolder(
                id=row['id'],
                name=row['name'],
            ),
            count=row['count'],
            percentage=row['percentage'],
            change=row['change'],
        ) for row in raw_data]

        return shareholders
