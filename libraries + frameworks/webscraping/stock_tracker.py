import os
import json
import requests
from bs4 import BeautifulSoup

result_companies = []
indexes = [2,4,5,12,17,18]
ratio_numbers = [10, 4, 8, 4]
#20, 5, 15, 7

url = 'https://finance.yahoo.com/quote/{}/key-statistics?p={}'


with open('companies2.json') as f:
    data = json.load(f)

for company in data:
    break_loop = False
    try:
        companie_symbol = company['Symbol']
    except:
        print(company)
        continue

    r = requests.get(url.format(companie_symbol, companie_symbol))
    bs4 = BeautifulSoup(r.content, 'html.parser')
    first_row = bs4.find(class_="Fl(start) W(50%) smartphone_W(100%)")

    try:
        company_name = bs4.find(class_="Mt(15px)").find('h1').text
        first_row_tables = first_row.find_all(class_="Fw(500) Ta(end) Pstart(10px) Miw(60px)")
    except:
        continue


    char_for_billion_company = 'B'
    index_for_revenue = 6

    #check if it is billion company
    if (char_for_billion_company not in first_row_tables[index_for_revenue].text):
        continue


    ratios = []

    for i in indexes:
        ratio = first_row_tables[i].text

        #remove all commas and replaced them with nothing
        ratio = ratio.replace(',', '')

        if ratio == 'N/A' or ratio == None:
            ratio = 'skip'

        #if % is in ratio, than cut it from it
        elif '%' in ratio:
            ratio = float(ratio[0:-1])
        else:
            ratio = float(ratio)

        ratios.append(ratio)

    if 'skip' in ratios:
        continue

    trues_or_falses = []

    for i, item in enumerate(ratios, 0):
        if item == ratios[4]:
            code = item < 200
        elif item == ratios[5]:
            code = item > 0.8 and item < 3.2
        else:
            code = item > ratio_numbers[i]

        trues_or_falses.append(code)


    #if list doesnt contains any Falses, than append to final list
    if False not in trues_or_falses:
        print(companie_symbol)
        result_companies.append(company_name)


with open('companies_result4.txt', 'w') as f:
    for company in result_companies:
        f.write(company)
        f.write('\n'*2)
