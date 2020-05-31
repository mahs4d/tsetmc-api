from bs4 import BeautifulSoup
import json
import re
import requests

intraday_pattern = re.compile("var (?P<name>.*)=(?P<content>\[[^;]*\]);")

def get_intraday_history(i, d):
    vars = {}

    daily_content = requests.get('http://cdn.tsetmc.com/Loader.aspx?ParTree=15131P&i={}&d={}'.format(i, d)).text

    all_scripts = BeautifulSoup(daily_content).find_all('script')

    first_script = str(all_scripts[-3])
    second_script = str(all_scripts[-2])
    third_script = str(all_scripts[-1])

    # first script
    matches = intraday_pattern.search(first_script)
    vars[matches.group('name')] = matches.group('content')

    # second script
    matches = intraday_pattern.findall(second_script)
    for match in matches:
        vars[match[0]] = json.loads(match[1].replace('\'', '"'))
    
    # third script
    matches = intraday_pattern.search(third_script)
    vars[matches.group('name')] = matches.group('content')
    
    return vars