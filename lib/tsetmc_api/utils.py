from copy import deepcopy

from jdatetime import date as jdate, time as jtime


def deep_update(d1: dict, d2: dict) -> dict:
    ret = deepcopy(d1)

    for key, value in d2.items():
        if key not in d1:
            ret[key] = value
        elif type(value) == dict:
            ret[key] = deep_update(d1=d1[key], d2=value)
        else:
            ret[key] = value

    return ret


def convert_heven_to_jtime(heven: int) -> jtime:
    heven = str(heven)
    if len(heven) == 6:
        return jtime(hour=int(heven[:2]), minute=int(heven[2:4]), second=int(heven[4:]))
    else:
        return jtime(hour=int(heven[:1]), minute=int(heven[1:3]), second=int(heven[3:]))


def convert_deven_to_jdate(deven: int) -> jdate:
    deven = str(deven)
    return jdate.fromgregorian(
        year=int(deven[:4]),
        month=int(deven[4:6]),
        day=int(deven[6:]),
    )
