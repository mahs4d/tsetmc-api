from datetime import datetime, time, date

from dateutil import tz as timezoneutil
from jdatetime import timedelta as jtimedelta, datetime as jdatetime

_timezone = timezoneutil.gettz('Asia/Tehran')


def get_timezone():
    return _timezone


def int_to_time(i: int) -> time:
    if isinstance(i, str):
        x = i
    else:
        x = str(i)

    if len(x) != 5:
        h = int(x[:2])
        m = int(x[2:4])
        s = int(x[4:])
    else:
        h = int(x[:1])
        m = int(x[1:3])
        s = int(x[3:])

    return time(hour=h, minute=m, second=s, tzinfo=get_timezone())


def get_timestamp(date: date, i: int) -> int:
    if isinstance(i, str):
        x = i
    else:
        x = str(i)

    if len(x) != 5:
        h = int(x[:2])
        m = int(x[2:4])
        s = int(x[4:])
    else:
        h = int(x[:1])
        m = int(x[1:3])
        s = int(x[3:])

    return int(datetime(year=date.year, month=date.month, day=date.day,
                        hour=h, minute=m, second=s, tzinfo=get_timezone()).timestamp())


def jalali_daterange(start_time: jdatetime, end_time: jdatetime):
    for n in range(int((end_time - start_time).days)):
        yield start_time + jtimedelta(n)
