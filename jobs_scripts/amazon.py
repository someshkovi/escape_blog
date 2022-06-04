from dataclasses import dataclass
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

search_parameter = 'laptop'

def get_amazon_results_by_search(search_parameter, no_of_pages=20):
    results = []
    for page in range(no_of_pages):
        link=f'https://www.amazon.in/s?k={search_parameter}&page={page}'
        page = requests.get(link, verify=False)

        soup = bs(page.content, 'html.parser')

        for d in soup.findAll('div', attrs={'class':'a-section'}):
            name = d.find('span', attrs={'class': 'a-size-medium a-color-base a-text-normal'})
            price = d.find('span', attrs={'class':'a-price-whole'})
            currency = d.find('span', attrs={'class':'a-price-symbol'})
            rating = d.find('span', attrs={'class':'a-icon-alt'})
            # ratings_count = d.find('span', attrs={'class':'a-size-base s-light-weight-text'})
            if name:
                try:
                    results.append({
                        'name':name.string,
                        'price':int(price.string.replace(',','')),
                        'currency':currency.string,
                        'rating':float(rating.string.split(' ')[0]),
                        # 'ratings_count':ratings_count.string,
                    })
                except Exception as e:
                    pass
    return results

def main():
    results = get_amazon_results_by_search('laptop', 20)
    df = pd.DataFrame(results)
    df = df.loc[:,~df.columns.duplicated()]
    df.to_csv('info.csv', index=False, encoding='utf-8')

@dataclass
class SearchResult():
    name:str
    price:int
    currency:str
    rating:float