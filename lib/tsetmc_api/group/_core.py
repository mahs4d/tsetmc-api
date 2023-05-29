from ..utils import safe_request, aio_safe_request


def get_group_static_data(response: dict = None) -> list[dict]:
    if response is None:
        response = safe_request(
            method='GET',
            url='http://cdn.tsetmc.com/api/StaticData/GetStaticData',
            params={},
            headers={
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
            },
            verify=False
        )
        response = response.json()['staticData']
    
    return response


async def aio_get_group_static_data() -> list[dict]:
    response = await aio_safe_request(
        method='GET',
        url='http://cdn.tsetmc.com/api/StaticData/GetStaticData',
        params={},
        headers={
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        },
        verify=False
    )
    response = (await response.json())['staticData']
    
    return get_group_static_data(response)
