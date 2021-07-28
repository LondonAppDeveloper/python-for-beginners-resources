import requests

DATA_URL = 'https://httpbin.org/get'


def get_data(name):
    """Retrieve data from API using HTTP."""
    params = {'name': name}
    res = requests.get(DATA_URL, params=params)

    return res.json()
