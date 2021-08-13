# -*- coding: utf8 -*-
import time

first = time.time()
while first + 5 >= time.time():
    pass
print("-" * 50)

# 배열 하나로 출력해보기
list = [
  [1,2,3],
  [4,5,6,7],
  [8,9],
]

for i in list :
  for j in i :
    print(j)