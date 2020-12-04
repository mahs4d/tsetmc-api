import locale
from datetime import date

import requests
from bs4 import BeautifulSoup


def get_client_type_history(symbol_id):
    raw = requests.get(f'http://www.tsetmc.com/tsev2/data/clienttype.aspx?i={symbol_id}',
                       timeout=20, verify=False).text
    raw_client_type_history = raw.split(';')

    ret = []
    for rsp in raw_client_type_history:
        ret.append(rsp.split(','))

    return ret


def get_major_shareholders(company_isin):
    raw = requests.get(f'http://www.tsetmc.com/Loader.aspx?Partree=15131T&c={company_isin}', timeout=20,
                       verify=False).text
    trs = BeautifulSoup(raw, 'lxml').find('tbody').find_all('tr')
    locale.setlocale(locale.LC_ALL, 'en_US.UTF8')

    ret = []
    for tr in trs:
        tds = tr.find_all('td')
        id = tr['onclick']
        id = id[id.index("'") + 1: id.index(",")]
        count = tds[1].find('div')['title']
        percentage = tds[2].contents[0]
        change = tds[3].contents[0]

        ret.append({
            'id': id,
            'name': str(tds[0].contents[0]),
            'shares_count': locale.atoi(count),
            'percentage': float(percentage),
            'change': locale.atoi(change),
        })

    return ret


def get_major_shareholder_details(company_isin, holder_id):
    raw = requests.get(f'http://www.tsetmc.com/tsev2/data/ShareHolder.aspx?i={holder_id}%2C{company_isin}',
                       timeout=20, verify=False).text
    raw = raw.split(';')

    ticks = []
    other_companies = []

    for z in raw:
        x = z.split(',')
        if len(x) == 2:
            ticks.append({
                'date': date(int(x[0][:4]), int(x[0][4:6]), int(x[0][6:])),
                'shares_count': int(x[1]),
            })
        elif len(x) == 4:
            other_companies.append({
                'symbol_id': x[0][1:] if '#' in x[0] else x[0],
                'company_name': x[1],
                'shares_count': int(x[2]),
                'percentage': float(x[3]),
            })

    return {
        'activities': ticks,
        'other_symbols': other_companies,
    }
