import os
import json
import requests
from bs4 import BeautifulSoup

url = 'https://www.aaii.com/stock/ticker/{}'
result_companies = []


with open('companies2.json') as f:
    data = json.load(f)

for company in data:
    break_loop = False
    try:
        company_symbol = company['Symbol']
        company_name = company['Company Name']
    except:
        continue

    r = requests.get(url.format(company_symbol))
    bs4 = BeautifulSoup(r.content, 'html.parser')

    try:
        container1 = bs4.find_all('table')[1].find_all('td')
        sales = container1[5].text
        sales = sales.replace(',', '')
        sales = float(sales[2:])
        
        container2 = bs4.find_all('table')[3].find_all('td')
        price_book = container2[5].text
        pe_ratio = container2[9].text

    except:
        continue

    
    if pe_ratio != 'na' and price_book != 'na' and sales > 700:
        pe_ratio = float(pe_ratio)
        price_book = float(price_book)
        
        if pe_ratio * price_book < 22.5:
            result_company = f'{company_name} - {company_symbol}'
            print(result_company)
            result_companies.append(result_company)
            
    else:
        continue
        
with open('undevalued_companies2.txt', 'w') as f:
    for company in result_companies:
        f.write(company)
        f.write('\n'*2)