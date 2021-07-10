# -*- coding: utf8 -*-

key_list = ["name", "hp", "mp", "level"]
value_list = ["준석용사", 500, 50, 5]
character = {}

for i in range(len(key_list)):
  character[key_list[i]] = value_list[i]

print(character)

limit = 10000
i = 1

sum_value = 0

#for 와 while의 차이점 : for 는 반복횟수를 알 때 사용한다.
while sum_value < limit :
  sum_value += i
  i += 1

print("{}를 더할 때 {}을 넘으며 그때의 값은 {}입니다.".format(i, limit, sum_value))