import requests


def get_group_static_data() -> list[dict]:
    response = requests.get(
        url='http://cdn.tsetmc.com/api/StaticData/GetStaticData',
        params={},
        verify=False,
timeout=20,
    )
    response.raise_for_status()
    response = response.json()['staticData']

    return response
