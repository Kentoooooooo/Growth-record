import requests
from bs4 import BeautifulSoup
from datetime import datetime


class Item:
    def __init__(self, name, price, release_date):
        self.name = name
        self.price = price
        self.release_date = release_date
        

url = 'https://docs.pyq.jp/_static/assets/scraping/item-list.html'
response = requests.get(url)
response.encoding = response.apparent_encoding

bs = BeautifulSoup(response.text, 'html.parser')

div_item_list = bs.select('div.item-list')

item_list = []

for div_item in div_item_list[0].select('div.item'):
    
    item_name_tags = div_item.select('a.item-name')
    item_name_tag = item_name_tags[0]
    item_name = item_name_tag.text.strip()
    
    item_price_tags = div_item.select('span.item-price')
    item_price_tag = item_price_tags[0]
    item_price = item_price_tag.text.strip()
    
    item_price = item_price.replace('円', '')
    item_price = item_price.replace(',', '')
    item_price = int(item_price)
    
    item_release_date_tags = div_item.select('span.item-release-date')
    item_release_date_tag = item_release_date_tags[0]
    item_release_date = item_release_date_tag.text.strip()
    item_release_date = datetime.strptime(item_release_date, '%Y-%m-%d')
    
    item_list.append(Item(item_name, item_price, item_release_date))
    
for item in item_list:
    from_date = datetime(2017, 5, 1)
    to_date = datetime(2017, 8, 31)
    if from_date <= item.release_date <= to_date:
        print(item.name, item.price)
    
