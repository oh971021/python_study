# -*- coding: utf8 -*-

numbers = [5,6,7,8,9,10,20,25]

for number in numbers :
  # number 가 10보다 작으면 다음 반복으로 넘어갑니다.
  if number < 10 :
    # 현재 반복을 중지하고, 다음 반복으로 넘어간다.
    # = for 문 안의 다른 코드는 실행하지 않는다.
    continue
  #출력합니다.
  print(number)