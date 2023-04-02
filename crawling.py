from selenium import webdriver
import time

## search in website what input keyworld
qeury_txt = input('enter the keyworld : ')
print('\n')

chrome_path = 'C:/Users/USER/PycharmProjects/pythonProject/chromedriver.exe'
driver = webdriver.Chrome(chrome_path)

url = 'http://www.riss.kr/'
driver.get(url)
time.sleep(2)

element = driver.find_element_by_id("query")
driver.find_element_by_id("query").click()
element.send_keys(qeury_txt)
element.send_keys('\n')

driver.find_element_by_link_text('학위논문').click()
time.sleep(2)


from bs4 import BeautifulSoup
html_1 = driver.page_source
soup_1 = BeautifulSoup(html_1, 'html.parser')

content_1 = soup_1.find('div', 'srchResultListW').find_all('li')
for i in content_1 :
  print(i.get_text().replace('\n',' ').strip())
  print('\n')

import sys
f_name = 'C:/Users/USER/Desktop/temp/test.txt'

orig_stdout = sys.stdout
file = open(f_name, 'a', encoding = 'utf-8')
sys.stdout = file

for i in content_1:
  print(i.get_text().replace('\n',''))

file.close()
sys.stdout = orig_stdout

print('complet and save file is %s,' %f_name)