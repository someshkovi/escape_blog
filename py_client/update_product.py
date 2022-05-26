import requests
import json
from requests.auth import HTTPBasicAuth

from getpass import getpass
username = 's'  #input('What is your username?\n')
password = 's'  #getpass('What is your password?\n')

url = "http://127.0.0.1:8000/products/2/"

payload = json.dumps({
  "url": "ff",
  "max_price": 59595
})
headers = {
  'Content-Type': 'application/json',
}

response = requests.request("put", url, headers=headers, data=payload, auth = HTTPBasicAuth('s', 's'))

print(response.json())
