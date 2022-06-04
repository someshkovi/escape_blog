import requests
from bs4 import BeautifulSoup
import unicodedata
import json
from db import get_connection, select_all_products

# from send_email import send_email


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

def get_amazon_product_info(url):
    page = requests.get(url, headers=headers, verify=False)
    soup = BeautifulSoup(page.content, features='lxml')
    try:
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
        json_response = json.dumps({
            'title':title,
            'price':price,
            'product_url':product_url,
            'availabity_messsage':availabity_messsage,
        })
        print(message)


def get_info_from_db():
    conn = get_connection()
    products = select_all_products(conn)
    for prod in products:
        store_update_price(prod[0])
    return products

def update_info_to_db():
    conn = get_connection()
    products = select_all_products(conn)


if __name__ == '__main__':
    url = 'https://www.amazon.in/Sony-WH-1000XM4-Cancelling-Headphones-Bluetooth/dp/B0863FR3S9/ref=sr_1_3?keywords=sony%2Bmx1000m4&qid=1652684397&sprefix=sony%2Bmx%2Caps%2C629&sr=8-3&th=1'
    # url = input('enter url: \n')
    # store_update_price(url, service='amazon.in')
    get_info_from_db()
