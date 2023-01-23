## Chapter 2. selenium

from selenium import webdriver
# driver = webdriver.Chrome(r'C:\Users\USER\Downloads\chromedriver\chromedriver.exe')

## Contect
# url = 'https://www.naver.com'
# driver.get(url)
# html = driver.page_source
# print(html)

## 예제로 HTML 구조 파악하기
# html = '''
# <html>
#     <head>
#     </head>
#     <body>
#         <h1> 우리동네시장</h1>
#             <div class = 'sale'>
#                 <p id='fruits1' class='fruits'>
#                     <span class = 'name'> 바나나 </span>
#                     <span class = 'price'> 3000원 </span>
#                     <span class = 'inventory'> 500개 </span>
#                     <span class = 'store'> 가나다상회 </span>
#                     <a href = 'http://bit.ly/forPlaywithData' > 홈페이지 </a>
#                 </p>
#             </div>
#             <div class = 'prepare'>
#                 <p id='fruits2' class='fruits'>
#                     <span class ='name'> 파인애플 </span>
#                 </p>
#             </div>
#     </body>
# </html>
# '''

## 태그 속성 활용하기
from bs4 import BeautifulSoup

# soup = BeautifulSoup(html, 'html.parser')
# print(soup)

# tags_span = soup.select('span')
# tags_p = soup.select('p')
# print(tags_span)
# print(tags_p)

# ids_fruits1 = soup.select('#fruits1')
# class_price = soup.select('.price')
# tags_span_class_price = soup.select('span.price')
# print(ids_fruits1)
# print(class_price)
# print(tags_span_class_price)

## 상위 구조 활용하기
# tags_name = soup.select('span.name')
# print(tags_name)
# tags_banana1 = soup.select('#fruits1 > span.name')
# print(tags_banana1)

# tags_banana2 = soup.select('div.sale > #fruits1 > span.name')
# tags_banana3 = soup.select('div.sale span.name')
# print(tags_banana2)
# print(tags_banana3)

## 정보 가져오기
# tags = soup.select('span.name')
# tag_1 = tags[0]
# tag_1 = tags[1]
# print(tag_1)

# for tag in tags:
#   print(tag)

# content = tag.text
# attribute = tag['속성명']

# tags = soup.select('a')
# tag = tags[0]
# content = tag.text
# print(content)
# link = tag['href']
# print(link)

## 멜론 노래 순위 정보 크롤링

# options = webdriver.ChromeOptions()
# options.add_argument("headless")
#
# driver = webdriver.Chrome(r'C:\Users\USER\Downloads\chromedriver\chromedriver.exe')
#
# url = 'https://www.melon.com/chart/index.htm'
# driver.get(url)
#
# html = driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
#
# # songs = soup.select('tr')
# # print(len(songs))
# # print(songs[1])
#
# songs = soup.select('tr')[1:]
# # print(len(songs))
# # print(songs[0])
#
# song = songs[0]
#
# # title = song.select('a')
# # print(len(title))
#
# # title = song.select('div.ellipsis.rank01 > span > a')
# # print(title)
#
# # for song in songs:
# #   title = song.select('div.ellipsis.rank01 > span > a')[0].text
# #   singer = song.select('div.ellipsis.rank02 > a')[0].text
# #   print(title, singer, sep = ' | ')
#
# driver.quit()

## 정리하기

## Header
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(r'C:\Users\USER\Downloads\chromedriver\chromedriver.exe')
url = 'https://www.melon.com/chart/index.htm'
driver.get(url)

## Body 1
# html = driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
#
# songs = soup.select('tr')[1:]
# for song in songs:
#   title = song.select('div.ellipsis.rank01 > span > a')[0].text
#   singer = song.select('div.ellipsis.rank02 > a')[0].text
#   print(title, singer, sep = ' | ')

## Body 2(훨씬 느림)
# songs = driver.find_elements_by_css_selector('tr')[1:]
#
# for song in songs:
#   title = song.find_elements_by_css_selector('div.ellipsis.rank01 > span > a')[0].text
#   singer = song.find_elements_by_css_selector('div.ellipsis.rank02 > a')[0].text
#   print(title, singer, sep = ' | ')

## Tail
driver.quit()