#### 1. Python Grammar for Coding Test

### 1-1. List

## List Comprehension.

# array = [i for i in range(20) if i % 2 == 1]
# print(array)

# array = [i * i for i in range(1, 10)]
# print(array)

# n = 3
# m = 4
# array = [[0] * m for _ in range(n)]
# print(array)
#
# ## 잘못된 초기화
# array = [[0] * m] * n
# print(array)
#
# array[1][1] = 5
# print(array)

## 반복문 내 언더바 : i 변수 값에 변동이 없는 경우 사용
# for _ in range(5):
#   print('Hell world')

# list method
# a = [1, 4, 3]
# print('first list : ', a)
#
# # 배열 끝에 추가
# a.append(2)
# print(a)
#
# # 오름차순 정렬
# a.sort()
# print(a)
#
# # 내림차순 정렬
# a.sort(reverse = True)
# print(a)
#
# # 배열 뒤집기
# a.reverse()
# print(a)
#
# #  특정 인덱스에 데이터 추가
# a.insert(2, 3)
# print(a)
#
# # 특정 값 데이터 수
# print('How Many Number 3 : ', a.count(3))
#
# # 특정 값 삭제
# a.remove(1)
# print(a)

## 특정 문자 지정하여 삭제하기
# a = [1,2,3,4,5,5,5]
# remove_set = {3,5}
#
# result = [i for i in a if i not in remove_set]
# print(result)

# data = 'Hell world'
# print(data)
#
# data = "Don't you konw \"Python\"?"
# print(data)

# 2. 퀵정렬
# array = [30, 35, 50, 45, 15, 25, 40]
#
# def quick_sort(array):
#   if len(array) <= 1: return array
#
#   pivot, value = array[0], array[1:]
#
#   leftSide = [x for x in value if x <= pivot]
#   rightSide = [x for x in value if x > pivot]
#
#   print('pivot', pivot)
#   print('value', value)
#   print('left', leftSide)
#   print('right', rightSide)
#
#   return quick_sort(leftSide) + [pivot] + quick_sort(rightSide)
#
# print(quick_sort(array))

# 3. 욕심쟁이

# def knapsack(capacity, n):
#   if capacity == 0 or n == 0:
#     return 0
#   if size[n-1] > capacity:
#     return knapsack(capacity, n-1)
#   else:
#     return max(value[n-1] + knapsack(capacity-size[n-1], n-1), knapsack(capacity, n-1))
#
# size = [7, 5, 4, 6, 2]
# value = [21, 20, 28, 36, 10]
#
# print(knapsack(20, 5)) # 14

# def knapsack1(capacity, n):
#   array = [[0 for _ in range(capacity+1)] for _ in range(n+1)]
#   for i in range(1, n+1):
#     for s in range(1, capacity+1):
#       if size[i-1] > s: # 물건의 부피가 s보다 크면
#         array[i][s] = array[i - 1][s]
#       else: # 물건의 부피가 s보다 작거나 같으면
#         array[i][s] = max(value[i-1] + array[i-1][s-size[i-1]], array[i-1][s])
#       print('%2d' % array[i][s], end=' ')
#     print()
#   return array[n][capacity]
#
# size = [7, 5, 4, 6, 2]
# value = [21, 20, 28, 36, 10]
#
# print(knapsack1(20, 5)) # 14

# # 3. 배낭 욕심쟁이 알고리즘
# N, W = 5, 20
# w = [7, 5, 4, 6, 2]
# b = [21, 20, 28, 36, 10]
#
# # 1kg당 가치를 저장할 배열 생성
# ratio = [[0, 0] for _ in range(N)] # 왼쪽은 ratio값, 오른쪽은 index를 저장한다
#
# # 1kg당 가치
# for i in range(N):
#     ratio[i][0] = b[i]/w[i]
#     ratio[i][1] = i
#     print(ratio[i])
#
# ans = 0
# for r in sorted(ratio, key=lambda x:-x[0]):
#     if w[r[1]] <= W:
#         print(W)
#         W -= w[r[1]]
#         ans += b[r[1]]
#         print(w[r[1]])
#     else:
#         ans += (W * r[0])
#         print((W * r[0]))
#         break
# print(ans)

import random
import time
from faker import Faker

text_user = 'INSERT INTO "USER" VALUES (USER_SEQ.NEXTVAL,'
text_goods = "INSERT INTO GOODS VALUES (GOODS_SEQ.NEXTVAL,"
text_board = 'INSERT INTO BOARD VALUES (BOARD_SEQ.NEXTVAL,'
fake = Faker('ko-KR')

def board():
  writer = random.randint(1, 11)
  title = fake.word()
  text = fake.text(80)
  date = fake.date()
  board = text_board + str(writer) + ',' + "'" + title + "', '" + text + "', '" + date + "');"
  return board

for i in range(10):
  print(board())

# def goods():
#   seller = random.randint(1, 11)
#   title = fake.word()
#   text = fake.text(80)
#   price = str(random.randint(10, 100)) + '0000'
#   date = fake.date()
#   god = text_goods + str(seller) + ',' + "'" + title + "'" + ', null' + ", '" + text + "', " + str(price) + ", '" + date + "');"
#   return god
#
# for i in range(11):
#   print(goods())

# def info():
#   name = fake.name()
#   id = fake.user_name()
#   tel = fake.phone_number()
#   birth = fake.date()
#   password = fake.word()
#   info = text_user + "'"+name+"', "+"'"+birth+"', "+"'"+id+"', "+"'"+password+"', "+"'"+tel+"');"
#   return info
#
# for i in range(11):
#   print(info())

