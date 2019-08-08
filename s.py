from selenium import webdriver
from bs4 import BeautifulSoup
from urllib import request
driver = webdriver.Chrome('D:\chromedriver')

driver.implicitly_wait(5)

driver.get('https://google.com')
driver.find_element_by_name('q').send_keys('구글뉴스')
driver.implicitly_wait(3)
driver.find_element_by_name('btnK').click()
driver.implicitly_wait(5)
driver.find_element_by_class_name('LC20lb').click()
driver.implicitly_wait(5)
driver.find_element_by_class_name('rdp59b').click()

html = request.urlopen(driver.current_url)
soup = BeautifulSoup(html.read(), 'html.parser')
select_title = soup.select('.ipQwMb ')
with open('d:wnews.txt','at', encoding='utf-8') as file:
    for i in select_title:
        file.write(i.text+',\n')

before = select_title[0].text
while(True):
    select_title2 = soup.select('.ipQwMb ')
    latest = select_title2[0].text
    if(before != latest):
        before = latest
        with open('d:wnews.txt', 'at', encoding='utf-8') as file:
            for i in select_title2:
                file.write(i.text+',\n')





