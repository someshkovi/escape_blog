import re

import requests

# endpoint = 'http://httpbin.org/status/200'
# endpoint = 'http://httpbin.org/anything'

endpoint = "http://localhost:8000/api/"

"""
{
  "args": {},
  "data": "",
  "files": {},
  "form": {},
  "headers": {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-IN,en-GB;q=0.9,en;q=0.8",
    "Host": "httpbin.org",
    "Sec-Ch-Ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"100\", \"Google Chrome\";v=\"100\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
    "X-Amzn-Trace-Id": "Root=1-626bc2c2-682f6da07c9629803289371d"
  },
  "json": null,
  "method": "GET",
  "origin": "106.217.144.9, 165.225.104.95",
  "url": "https://httpbin.org/anything"
}
"""
# get_response = requests.get(endpoint, params={"id": 123}, json={"query":"Hello World!"})  # Http Request
get_response = requests.post(endpoint, json={"title": "Hello 3"})
print(get_response.json())
print(get_response.status_code)
