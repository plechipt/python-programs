import ctypes
import requests
import win32gui, win32con
from bs4 import BeautifulSoup
from win10toast import ToastNotifier

# Hide python console
the_program_to_hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(the_program_to_hide , win32con.SW_HIDE)

toaster = ToastNotifier()
url = requests.get('https://www.myprotein.cz/sports-nutrition/impact-whey-protein/10530943.html?fbclid=IwAR1LpOH4TqGoybbgsc9yvmM1HILm4-BCY-Lt5LMCSWGCuhI2LjYeVF4yWzQ')
bs = BeautifulSoup(url.content, 'html.parser')

container = bs.find(class_='stripBanner_text')
price_container = container.find('p')

# Indexes to get price
ending_index = price_container.text.index('%', 10)
starting_index = ending_index - 2

# Get final price
final_price = int(price_container.text[starting_index:ending_index])

# If price is same or bigger than 45 -> notify
if final_price >= 45:
    toaster.show_toast('MYPROTEIN sleva!', 'nice')
