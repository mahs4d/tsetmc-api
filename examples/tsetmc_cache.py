#! /usr/bin/python3
import json
from datetime import timedelta, date

from tsetmc_api import Asset

assets = Asset.get_assets()

errors = []


def load_day(year, month, day):
    for asset in assets:
        try:
            print(f'loading {asset.asset_id} > {year}/{month}/{day}')
            asset.get_day_details(year, month, day)
        except ValueError as ex:
            print(ex)
        except Exception as ex:
            print(ex)
            errors.append({'id': asset.asset_id, 'day': f'{year}/{month}/{day}', 'ex': str(ex)})


def load_day_range(start_date, end_date):
    def daterange(start_date, end_date):
        for n in range(int((end_date - start_date).days)):
            yield start_date + timedelta(n)

    for single_date in daterange(start_date, end_date):
        load_day(single_date.year, single_date.month, single_date.day)


def main():
    start_date = date(2018, 3, 21)
    end_date = date(2019, 3, 21)
    load_day_range(start_date, end_date)


if __name__ == '__main__':
    main()
    with open('errors.json', 'w') as fp:
        json.dump(errors, fp)
