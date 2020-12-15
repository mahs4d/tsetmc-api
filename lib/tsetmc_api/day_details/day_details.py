from datetime import timedelta, datetime
from typing import List, Optional, Dict

from jdatetime import date, time

from tsetmc_api.cache import PersistentCache
from tsetmc_api.shareholder import SymbolMajorShareholder
from tsetmc_api.utils import get_timezone
from . import core as day_details_core
from .exceptions import NoDataError
from .snapshot import Snapshot
from .trade import Trade


class SymbolDayDetails:
    def __init__(self, symbol, jyear: int, jmonth: int, jday: int,
                 load_from_cache: bool = True, save_to_cache: bool = True, save_raw_data: bool = False):
        self.symbol = symbol
        self.date = date(year=jyear, month=jmonth, day=jday)
        self.greg_date = self.date.togregorian()
        self.load_from_cache = load_from_cache
        self.save_to_cache = save_to_cache
        self.save_raw_data = save_raw_data

        self._is_no_data = False

        self._load()

    def _load(self):
        if self._load_from_cache():
            return

        self._load_from_tsetmc()

    def _load_from_cache(self) -> bool:
        if not self.load_from_cache:
            return False

        if PersistentCache.exists('symbol_day_details', self._get_cache_minor(is_raw=False)):
            f = PersistentCache.fetch('symbol_day_details', self._get_cache_minor(is_raw=False))

            if 'no_data' in f:
                self._is_no_data = True
                raise NoDataError('there is no data for this symbol in the specified date')

            self._final_shareholders = f['final_shareholders']
            self._initial_shareholders = f['initial_shareholders']
            self._trades = f['trades']
            self._snapshots = f['snapshots']
            return True
        elif PersistentCache.exists('symbol_day_details', self._get_cache_minor(is_raw=True)):
            f = PersistentCache.fetch('symbol_day_details', self._get_cache_minor(is_raw=True))

            if 'no_data' in f:
                self._is_no_data = True
                raise NoDataError('there is no data for this symbol in the specified date')

            self._load_from_raw_data(**f)
            return True

        return False

    def _load_from_tsetmc(self):
        mdate = self.date.togregorian()
        try:
            data = day_details_core.load_intraday_data(self.symbol.id, mdate.year, mdate.month, mdate.day)
        except NoDataError as ex:
            self._is_no_data = True
            self._save_to_cache()
            raise ex

        company_isin = self.symbol.get_details()['company_isin']

        self._load_from_raw_data(company_isin=company_isin, raw_data=data)

        self._save_to_cache(is_raw=self.save_raw_data, raw_data={
            'company_isin': company_isin,
            'raw_data': data,
        })

    def _load_from_raw_data(self, company_isin: str, raw_data: Dict):
        self._final_shareholders = []
        for shdata in raw_data['shareholders']:
            self._final_shareholders.append(SymbolMajorShareholder(self.symbol.id,
                                                                   company_isin=company_isin,
                                                                   holder_name=shdata['name'],
                                                                   holder_id=shdata['id'],
                                                                   percentage=shdata['percentage'],
                                                                   shares_count=shdata['shares_count']))

        self._initial_shareholders = []
        for shdata in raw_data['previous_shareholders']:
            self._initial_shareholders.append(SymbolMajorShareholder(self.symbol.id,
                                                                     company_isin=company_isin,
                                                                     holder_name=shdata['name'],
                                                                     holder_id=shdata['id'],
                                                                     percentage=shdata['percentage'],
                                                                     shares_count=shdata['shares_count']))

        self._trades = Trade.from_raw_trades_data(raw_data['trades'])

        self._snapshots = list(
            Snapshot.generate_snapshots_from_raw_day_detail_data(self.greg_date,
                                                                 raw_data['price_data'],
                                                                 raw_data['orders_data'])
        )

    def _save_to_cache(self, is_raw: bool = False, raw_data: Optional[Dict] = None):
        if not self.save_to_cache:
            return

        if self._is_no_data:
            PersistentCache.store('symbol_day_details', self._get_cache_minor(is_raw=is_raw), {
                'no_data': True,
            })
            return

        if is_raw:
            PersistentCache.store('symbol_day_details', self._get_cache_minor(is_raw=True), raw_data)
        else:
            PersistentCache.store('symbol_day_details', self._get_cache_minor(is_raw=False), {
                'final_shareholders': self._final_shareholders,
                'initial_shareholders': self._initial_shareholders,
                'trades': self._trades,
                'snapshots': self._snapshots,
            })

    def _get_cache_minor(self, is_raw: bool = False):
        if is_raw:
            return f'{self.symbol.id}-{self.date.year}-{self.date.month}-{self.date.day}'
        else:
            return f'{self.symbol.id}-{self.date.year}-{self.date.month}-{self.date.day}-raw'

    def get_final_major_shareholders(self) -> List[SymbolMajorShareholder]:
        """
        سهامداران عمده در پایان روز
        """
        if self._is_no_data:
            return []

        return self._final_shareholders

    def get_initial_major_shareholders(self) -> List[SymbolMajorShareholder]:
        """
        سهامداران عمده در ابتدای روز
        """
        if self._is_no_data:
            return []

        return self._initial_shareholders

    def get_trades(self) -> List[Trade]:
        """
        معاملات
        """
        if self._is_no_data:
            return []

        return self._trades

    def get_snapshots(self) -> List[Snapshot]:
        """
        تمام لحظات سهم در طور روز
        """
        if self._is_no_data:
            return []

        return self._snapshots

    def get_snapshots_by_time(self, hour: int, minute: int, second: int) -> List[Snapshot]:
        """
        وضعیت سهم در زمان خاصی از روز
        """
        if self._is_no_data:
            return []

        snapshots = []
        t = int(datetime(year=self.greg_date.year, month=self.greg_date.month, day=self.greg_date.day,
                         hour=hour, minute=minute, second=second, tzinfo=get_timezone()).timestamp())
        last_snapshot = None
        for snapshot in self._snapshots:
            if snapshot.time > t:
                if not snapshots:
                    return [last_snapshot]

                return snapshots

            if snapshot.time == t:
                snapshots.append(snapshot)

            last_snapshot = snapshot

        if not snapshots:
            return [last_snapshot]

        return snapshots

    def get_snapshots_by_rate(self, from_time: time, to_time: time, delta: timedelta) -> List[Snapshot]:
        """
        وضعیت سهم در لحظات مختلف روز در بازه‌هایی با طول pick_rate
        """
        if self._is_no_data:
            return []

        ret = []
        start_datetime = datetime(year=self.greg_date.year, month=self.greg_date.month, day=self.greg_date.day,
                                  hour=from_time.hour, minute=from_time.minute, second=from_time.second,
                                  tzinfo=get_timezone())
        end_timestamp = int(datetime(year=self.greg_date.year, month=self.greg_date.month, day=self.greg_date.day,
                                     hour=to_time.hour, minute=to_time.minute, second=to_time.second,
                                     tzinfo=get_timezone()).timestamp())
        next_pick_datetime = start_datetime
        next_pick_timestamp = int(start_datetime.timestamp())
        last_snapshot = None
        for snapshot in self.get_snapshots():
            if snapshot.time > next_pick_timestamp:
                if last_snapshot:
                    snapshot_copy = last_snapshot.copy()
                    snapshot_copy.time = next_pick_timestamp
                    ret.append(snapshot_copy)
                    next_pick_datetime += delta
                    next_pick_timestamp = int(next_pick_datetime.timestamp())

            last_snapshot = snapshot
            if next_pick_timestamp > end_timestamp:
                break

        return ret
