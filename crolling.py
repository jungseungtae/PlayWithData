### 웹크롤링 맛보기 ###

from selenium import webdriver

driver = webdriver.Chrome('C:/Users/USER/PycharmProjects/pythonProject/chromedriver.exe')

url = 'https://www.naver.com/'
driver.get(url)

html = driver.page_source

from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'html.parser')

# print(soup)

# tags_span = soup.select('span')
# tags_p = soup.select('p')

# print(tags_span)

