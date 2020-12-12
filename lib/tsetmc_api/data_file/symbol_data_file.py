from __future__ import annotations

import pickle
import zipfile
from dataclasses import dataclass

from jdatetime import datetime as jdatetime

from tsetmc_api.cache import PersistentCache
from tsetmc_api.day_details.day_details import SymbolDayDetails
from tsetmc_api.day_details.exceptions import NoDataError
from tsetmc_api.symbol import Symbol
from tsetmc_api.types import SymbolId
from tsetmc_api.utils import jalali_daterange


@dataclass
class SymbolDataFileInformation:
    symbol_id: SymbolId
    start_time: jdatetime
    end_time: jdatetime


class SymbolDataFile:
    @staticmethod
    def get_data_file_information(file_location: str) -> SymbolDataFileInformation:
        with zipfile.ZipFile(file_location, 'r') as zp:
            with zp.open('information.pickle', 'r') as infop:
                return pickle.load(infop)

    @staticmethod
    def install_data_file(file_location: str):
        file_information = SymbolDataFile.get_data_file_information(file_location=file_location)
        with zipfile.ZipFile(file_location, 'r') as zp:
            for jdate in jalali_daterange(start_time=file_information.start_time, end_time=file_information.end_time):
                print(f'Installing {jdate.year}/{jdate.month}/{jdate.day}')
                file_name = f'{jdate.year}-{jdate.month}-{jdate.day}.pickle'
                try:
                    with zp.open(file_name, 'r') as pfp:
                        day_details = pickle.load(pfp)
                        if type(day_details) == SymbolDayDetails:
                            day_details._save_to_cache()
                        else:
                            PersistentCache.store(
                                'symbol_day_details',
                                f'{file_information.symbol_id}-{jdate.year}-{jdate.month}-{jdate.day}',
                                {
                                    'no_data': True,
                                }
                            )
                except KeyError:
                    pass
                except Exception as ex:
                    print(type(ex))
                    print(ex)

    @staticmethod
    def generate_data_file(symbol_id: SymbolId, start_time: jdatetime, end_time: jdatetime, file_location: str):
        symbol = Symbol(symbol_id=symbol_id)
        with zipfile.ZipFile(file_location, 'w') as zp:
            for jdate in jalali_daterange(start_time=start_time, end_time=end_time):
                while True:
                    print(f'Loading {jdate.year}/{jdate.month}/{jdate.day}')
                    file_name = f'{jdate.year}-{jdate.month}-{jdate.day}.pickle'
                    try:
                        day_details = symbol.get_day_details(jyear=jdate.year, jmonth=jdate.month, jday=jdate.day)
                        with zp.open(file_name, 'w') as pfp:
                            pickle.dump(day_details, pfp)
                        break
                    except NoDataError as ex:
                        with zp.open(file_name, 'w') as pfp:
                            pickle.dump(None, pfp)
                        break
                    except Exception as ex:
                        print(ex)

            with zp.open('information.pickle', 'w') as infop:
                pickle.dump(SymbolDataFileInformation(
                    symbol_id=symbol_id,
                    start_time=start_time,
                    end_time=end_time,
                ), infop)
