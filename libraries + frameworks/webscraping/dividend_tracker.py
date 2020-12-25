import time
import datetime
import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier

#for noticing stock is down
toaster = ToastNotifier() 

tickers = [
    'AAPL', 'ABBV', 'BAC', 'D', 'DUK', 'JNJ', 'JPM', 'KO', 'MSFT', 'O', 'PEP',
    'PFE', 'SBUX', 'SO', 'SPG', 'STOR', 'T', 'UPS', 'VTR', 'VZ', 'WELL', 'WPC'
]

current_date = datetime.date.today().strftime('%m/%d/%Y')

for ticker in tickers:
    url = requests.get(f'https://seekingalpha.com/symbol/{ticker}/dividends/scorecard')
    bs4 = BeautifulSoup(url.content, 'html.parser')

    container = bs4.find(class_="dividends-tab dividends")

    if container != None:
        section = container.find_all('section')[1]
        print(section.find(class_='highlighted'))
        pass
        #print(dividend_row)
        

    '''
    if stock_price < entry_price:
        #notify user the stock is down
        toaster.show_toast(f'{ticker} stock', f'is down {stock_price}!')
    '''