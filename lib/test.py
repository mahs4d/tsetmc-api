from jdatetime import time, timedelta

from tsetmc_api.symbol import Symbol
from tsetmc_api.utils import get_timezone

a = Symbol('22560050433388046')
c = a.get_day_details(1399, 9, 5).get_snapshots_by_rate(time(8, 0, 0, tzinfo=get_timezone()),
                                                        time(14, 0, 0, tzinfo=get_timezone()),
                                                        timedelta(seconds=300))
print(c[40])
