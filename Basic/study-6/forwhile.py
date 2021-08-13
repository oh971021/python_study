# -*- coding: utf8 -*-
# map 을 순환문을 돌리면 key 값만 가져온다.
for i in {'a':1, 'b':2} :
  print(i, end=" ")

i = 0
while True:
  i += 1
  print(i)
  if i == 100 :
    print("빠져나오자")
    break

j = int(input("정수 20을 써보세요 : "))

print("훌륭합니다") if j == 20 else print("다시 입력해주세요")