import requests
from bs4 import BeautifulSoup
import os

url = requests.get('https://kytary.cz/kytary/elektricke-kytary/st-modely/?PurchaseRateOrdering=1')
bs = BeautifulSoup(url.content, 'html.parser')

guitar_items = bs.find_all(class_="product-list__item") # finding all guitar objects
guitar_infos = []

for name, price in zip(guitar_items, guitar_items):
    if len(guitar_infos) >= 12: # looping 12 guitar objects
        break
    name = name.find(class_="delta margin--null").get_text() # scraping name
    price = price.find(class_="price").get_text() # scraping price
    guitar_infos.append(f'{name}  -->  {price}')

os.chdir(r'C:\Users\plech\Desktop')

with open('guitars.txt', 'w') as f: # saving all info to file on desktop
    for guitar in guitar_infos:
        f.write(guitar)
        f.write('\n'*2)
