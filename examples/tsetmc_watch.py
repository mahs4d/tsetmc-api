#! /usr/bin/python3
import datetime
import os
import pickle
from datetime import timedelta, date
from os import path

from dateutil import tz as timezoneutil

from tsetmc_api import Asset

"""
watch event format: {
    t: timestamp
    payload: { data: [{
        id, t, o, c, l, h, lst, y, cnt, v, s, buy: [{t, cnt, v, p}], sell: <same as buy>,
    }]}
}
"""

tz = timezoneutil.gettz('Asia/Tehran')


def to_timestamp(year, month, day, pt):
    z = str(pt)
    if len(z) == 5:
        hour = int(z[:1])
        minute = int(z[1:3])
        second = int(z[3:])
        timestamp = datetime.datetime(year, month, day, hour, minute, second, 0, tzinfo=tz)
    else:
        hour = int(z[:2])
        minute = int(z[2:4])
        second = int(z[4:])
        timestamp = datetime.datetime(year, month, day, hour, minute, second, 0, tzinfo=tz)

    return int(timestamp.timestamp())


def generate_watch_events(assets, year, month, day, pick_times):
    events = []
    pick_times.sort()
    for pt in pick_times:
        timestamp = to_timestamp(year, month, day, pt)
        events.append({
            't': timestamp,
            'payload': {'assets': []}
        })

    for asset in assets:
        try:
            details = asset.get_day_details(year, month, day)
            picked_snapshots = details.pick_snapshots_at(pick_times)

            for i, picked_snapshot in enumerate(picked_snapshots):
                picked_snapshot['id'] = asset.asset_id
                events[i]['payload']['assets'].append(picked_snapshot)
        except ValueError:
            continue

    return events


def watch_events(assets, start_date, end_date, pick_times, save_path):
    def daterange(start_date, end_date):
        for n in range(int((end_date - start_date).days)):
            yield start_date + timedelta(n)

    for single_date in daterange(start_date, end_date):
        print(f'extracting watch events @{single_date.year}/{single_date.month:02}/{single_date.day:02}')
        events = generate_watch_events(assets, single_date.year, single_date.month, single_date.day, pick_times)
        with open(path.join(save_path, f'{single_date.year}{single_date.month:02}{single_date.day:02}.pickle'),
                  'wb') as fp:
            pickle.dump(events, fp)


def main():
    assets = Asset.get_assets()
    start_date = date(2018, 3, 21)
    end_date = date(2019, 3, 21)
    pick_times = [90000, 93000, 100000, 103000, 110000, 113000, 120000, 123000]
    save_path = path.expanduser('~/.tsetmc-api/watch_events')
    os.makedirs(save_path, exist_ok=True)
    watch_events(assets, start_date, end_date, pick_times, save_path)


if __name__ == '__main__':
    main()
