import sys

from jdatetime import datetime as jdatetime

from tsetmc_api.data_file import SymbolDataFile
from tsetmc_api.types import SymbolId


def generate(symbol_id: SymbolId, start_time: jdatetime, end_time: jdatetime):
    file_name = f'{symbol_id}_{start_time.strftime("%Y%m%d")}_{end_time.strftime("%Y%m%d")}.zip'
    print(f'Generating Data File {file_name} ...')
    SymbolDataFile.generate_data_file(symbol_id=symbol_id,
                                      start_time=start_time,
                                      end_time=end_time,
                                      file_location=file_name)


def install(file_location: str):
    SymbolDataFile.install_data_file(file_location)


def main():
    if len(sys.argv) < 2:
        print('not enough arguments')
        sys.exit(1)

    action = sys.argv[1]
    if action == 'generate':
        if len(sys.argv) <= 2:
            print('symbol id was not provided')
            sys.exit(1)

        symbol_id = sys.argv[2]

        if len(sys.argv) > 3:
            start_time = jdatetime.strptime(sys.argv[3], '%Y-%m-%d')
        else:
            start_time = jdatetime(1396, 1, 1)

        if len(sys.argv) > 4:
            end_time = jdatetime.strptime(sys.argv[4], '%Y-%m-%d')
        else:
            end_time = jdatetime.now()

        generate(symbol_id=symbol_id, start_time=start_time, end_time=end_time)
    elif action == 'install':
        if len(sys.argv) <= 2:
            print('file location was not provided')
            sys.exit(1)

        file_location = sys.argv[2]
        install(file_location=file_location)
    else:
        print('invalid action')
        sys.exit(1)
