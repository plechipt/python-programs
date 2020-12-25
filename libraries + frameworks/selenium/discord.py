from selenium import webdriver
from bs4 import BeautifulSoup
import random
import string
from time import sleep

random_string = ''
alphabet_len = 25
alphabet = string.ascii_uppercase

def random_int(x):
    return random.randint(0, x)

def random_letters():
    return alphabet[random_int(alphabet_len)]

for i in range(10):
    random_string += random_letters()

print(random_string)

browser = webdriver.Chrome()
browser.get('https://discordapp.com/register')

email = browser.find_element_by_name('email')
username = browser.find_element_by_name('username')
password = browser.find_element_by_name('password')
check_box = browser.find_element_by_xpath('/html/body/div/div[1]/div/div[3]/div/form/div/div[2]/div[4]/label/input').click()
continue_bar = browser.find_element_by_xpath('/html/body/div/div[1]/div/div[3]/div/form/div/div[2]/div[5]/button')

email.send_keys(f'jacob{random_int(100)}@gmail.com')
username.send_keys(f'Jman{random_int(100)}')
password.send_keys(random_string)
#check_box.click()
#continue_bar.click()
