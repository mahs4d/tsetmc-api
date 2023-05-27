import requests


def get_group_static_data() -> list[dict]:
    response = requests.get(
        url='http://cdn.tsetmc.com/api/StaticData/GetStaticData',
        params={},
        headers={
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        },
        verify=False,
        timeout=20,
    )
    response.raise_for_status()
    response = response.json()['staticData']

    return response
