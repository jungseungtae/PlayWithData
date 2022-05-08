### 1. 반복문

## 1-1. for

# result = 0
# for i in range(11):
#   result += i
# print(result)

# for i in range(2, 10):
#   for j in range(1, 10):
#     # print(i*j)
#     print(i, '*', j, ' = ', i * j)
#   print()

## 1-2 while

# i = 1
# while i < 11:
#   print(i, end=' ')
#   i = i + 1

# i = 1
# while i < 10:
#   print(i, end=' ')
#   i += 2

# i = 9
# while i > 0:
#   print(i, end=' ')
#   i -= 2

# i = 1
# result = 0
# while i < 11:
#   result += i
#   i += 1
# print(result)

# i = 2
# while i < 10:
#   j = 1
#   while j < 10:
#     print(i, '*', j, ' = ', i * j)
#     j += 1
#   i += 1
#   print()

# i = 2
# while i < 10:
#   print()
#   j = 1
#   while j < 10:
#     print('{} * {} = {}'.format(i, j, i * j))
#     j += 1
#   i += 1

### 2. 조건문

## 2-1. if

# x = 6
# if x > 5:
#   print('True')

# x = 4

# if x > 5:
#   print('True')
# else:
#   print('False')

# x = 4
#
# if x < 5:
#   print('5 미만')
# else:
#   print('5 이상')

x = 4

if x < 5:
  pass
elif x == 5:
  print(5)
else:
  print('5 over')