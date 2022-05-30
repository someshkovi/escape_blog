import re
import requests
import json
from requests.auth import HTTPBasicAuth
if __name__=='__main__':
    from getpass import getpass
    username = 's'  #input('What is your username?\n')
    password = 's'  #getpass('What is your password?\n')

    url = "http://127.0.0.1:8000/products/6/"

    price = 0

    payload = json.dumps({
      "price": price
    })
    headers = {
      'Content-Type': 'application/json',
    }

    response = requests.request("put", url, headers=headers, data=payload, auth = HTTPBasicAuth('s', 's'))

    print(response.json())


def put_product_data(url, data, username, password):
	try:
		payload = json.dumps(data)
		headers = {
			'Content-Type': 'application/json',
		}
		response = requests.request("PATCH", url, headers=headers, data=payload, auth = HTTPBasicAuth(username, password))
		return response.json()
	except Exception as e:
		print(e)
		return {'error':e}