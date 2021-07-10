# -*- coding: utf8 -*-

## 학습내용 ##

# min(리스트) or min(숫자, 숫자, 숫자, ...)
# max(리스트) or max(숫자, 숫자, 숫자, ...)
# sum(리스트)
# for i in reversed(리스트):
# for i, element in enumerate(리스트):
# for key, value in dictionary.items():

#### 일회용 함수 : 제너레이터 ####

# 리스트 뒤집기 함수 : reversed()
a = [0,4,5,7,8,10]
reversed_a = reversed(a)
  # print(list(reversed_a))
  # print(list(reversed_a))
for i in reversed_a:
  print(i, end=" ")
print()
# 빈 깡통이 되서 위에서 한번 사용하면 값이 사라진다.
for i in reversed_a:
  print(i, end=" ")
print("---")
# 일회용 함수라서 두번 사용하면 값이 출력되지 않는다.
enumerate_a = enumerate(a)
for (i, element) in enumerate_a:
  print("{}번째 요소는 {}입니다.".format(i, element))
print("---")
for (i, element) in enumerate_a:
  print("{}번째 요소는 {}입니다.".format(i, element))

# items 함수
a = {
  "key_1": "value_1",
  "key_2": "value_2",
  "key_3": "value_3"
}

for key, value in a.items():
  print("{}키의 값은 {}입니다.".format(key,value))