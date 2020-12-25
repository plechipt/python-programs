import requests
from bs4 import BeautifulSoup

user_input = input('\n Enter a product: ')
url = requests.get(f'https://aukro.cz/vysledky-vyhledavani?text={user_input}')

bs4 = BeautifulSoup(url.content, 'lxml')
print(bs4)


