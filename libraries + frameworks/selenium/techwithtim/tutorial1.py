from selenium import webdriver
import time

PATH = r"C:\Users\Admin\Downloads\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get('https://youtube.com')

time.sleep(3)

dismiss_button = driver.find_element_by_xpath('//*[@id="dismiss-button"]/yt-button-renderer/a]')
dismiss_button.click()


