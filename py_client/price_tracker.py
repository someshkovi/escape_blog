import requests
from bs4 import BeautifulSoup
import unicodedata
import json

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}


def get_amazon_product_info(url):
    try:
        page = requests.get(url, headers=headers, verify=False)
        soup = BeautifulSoup(page.content, features='lxml')
        title = soup.find(id='productTitle').get_text().strip()
        price_str = soup.find(id='tp_price_block_total_price_ww').get_text()
    except Exception as e:
        error_msg = f'exception in getting product info = {e}'
        return None, None, None, None

    try:
        availabity_messsage = soup.select('#availability .a-color-success')[0].get_text().strip()
        available=True
    except:
        try:
            availabity_messsage = soup.select('#availability .a-color-price')[0].get_text().strip()
            available=True
        except:
            availabity_messsage = None
            available=False

    try:
        price = unicodedata.normalize('NFKD', price_str)
        price = price.split('.')[0].replace(',','').replace('₹', '')
        price = float(price)
    except:
        return None, None, None, None
    
    return title, price, available, availabity_messsage

def store_update_price(product_url, service='amazon.in', limit=10_00_00_000):
    if service == 'amazon.in':
        title, price, available ,availabity_messsage= get_amazon_product_info(product_url)
    else:
        title, price, available ,availabity_messsage = None, None, None, None
    if title is not None and price < limit and available:
        message = f'Price below limit : \n {title} \n Price: {price} \n {product_url} \n\n'
        response = {
            'title':title,
            'price':price,
            'product_url':product_url,
            'availabity_messsage':availabity_messsage,
        }
        return response
        # print(message)
    return {'error': 'unable to fetch data'}
