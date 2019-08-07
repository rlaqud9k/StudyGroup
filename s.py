from selenium import webdriver
from bs4 import BeautifulSoup
from urllib import request
driver = webdriver.Chrome('D:\chromedriver')

driver.implicitly_wait(3)

driver.get('https://google.com')
driver.find_element_by_name('q').send_keys('구글뉴스')
driver.find_element_by_name('btnK').click()
driver.find_element_by_class_name('LC20lb').click()
html = driver.current_url
soup = BeautifulSoup(request.urlopen(html))
print(soup.text)