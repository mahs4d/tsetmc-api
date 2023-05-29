from aiohttp import ClientSession
from copy import deepcopy
from jdatetime import date as jdate, time as jtime
from requests import request
from requests.exceptions import HTTPError


def safe_request(method, url, timeout=20, **kwargs):
    res = request(method.upper(), url, timeout=timeout, **kwargs)
    res.raise_for_status()
    return res


async def aio_safe_request(method, url, timeout=20, **kwargs):
    if 'verify' in kwargs:
        kwargs['ssl'] = kwargs.pop('verify')
    else:
        kwargs.setdefault('ssl', True)
    
    async with ClientSession() as session:
        # noinspection PyProtectedMember
        response = await session._request(method.upper(), url, timeout=timeout, **kwargs)
        response.text = await response.text()
        response.close()
    
    response.status_code = response.status
    
    # region raise_for_status()
    http_error_msg = ""
    if isinstance(response.reason, bytes):
        # We attempt to decode utf-8 first because some servers
        # choose to localize their reason strings. If the string
        # isn't utf-8, we fall back to iso-8859-1 for all other
        # encodings. (See PR #3538)
        try:
            reason = response.reason.decode("utf-8")
        except UnicodeDecodeError:
            reason = response.reason.decode("iso-8859-1")
    else:
        reason = response.reason
    
    if 400 <= response.status_code < 500:
        http_error_msg = (
            f"{response.status_code} Client Error: {reason} for url: {response.url}"
        )
    
    elif 500 <= response.status_code < 600:
        http_error_msg = (
            f"{response.status_code} Server Error: {reason} for url: {response.url}"
        )
    
    if http_error_msg:
        raise HTTPError(http_error_msg, response=response)
    # endregion
    
    return response


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
