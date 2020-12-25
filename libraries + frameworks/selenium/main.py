from selenium import webdriver
from bs4 import BeautifulSoup

browser = webdriver.Chrome()
browser.get('https://www.youtube.com')
search_box = browser.find_element_by_xpath('//*[@id="search"]')
click_box = browser.find_element_by_xpath('//*[@id="search-icon-legacy"]')

search_box.send_keys('Django')
click_box.click()

for video in browser.find_element_by_xpath('//*[@id="contents"]'):
    print(video.text)
