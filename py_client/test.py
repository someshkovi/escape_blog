# import requests
# import json
# from requests.auth import HTTPBasicAuth


# url = "http://127.0.0.1:8000/products/2/"

# payload = json.dumps({
#   "url": "ff",
#   "name": "dfdf"
# })
# headers = {
#   'Content-Type': 'application/json',
# }

# response = requests.request("put", url, headers=headers, data=payload, auth = HTTPBasicAuth('s', 's'))

# print(response.text)

from product_update_data import put_product_data
from product_get_data import get_product_data
from price_tracker import store_update_price
endpoint = 'http://127.0.0.1:8000/api/v1/products/'
url = endpoint+'6'+'/'
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
	put_response = put_product_data(url, data, 's', 's')
	# print(put_response)