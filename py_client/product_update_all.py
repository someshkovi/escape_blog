import environ
import os
import requests
from pathlib import Path
from product_update_data import put_product_data
from product_get_data import get_product_data
from price_tracker import store_update_price


env = environ.Env()
CORE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(os.path.join(CORE_DIR, '.env'))
if 'hostname' in env and 'port' in env:
    hostname = env('hostname')
    port = env('port')
    http = env('http')
    endpoint = f'{http}://{hostname}:{str(port)}/api/v1/products/'
else:
    endpoint = 'http://127.0.0.1:8000/api/v1/products/'

if 'username' in env:
    username = env('username')
    password = env('password')
else:
    username = 's'
    password = 's'

response = requests.request("GET",endpoint, headers={}, data={})

json_respone = response.json()
for item in json_respone:
    id = item.get('id')
    if id is not None:
        url = endpoint+str(id)+'/'
        response = get_product_data(url)
        if response.get('url') is not None:
            product_url = response.get('url')
            scrapper_respone = store_update_price(product_url)
            if scrapper_respone.get('price') is not None:
                price = scrapper_respone.get('price')
                availability_message = scrapper_respone.get('availability_message')
                data = {
                    'price': price,
                    'availability_message':availability_message,
                }
                put_response = put_product_data(url, data, username, password)