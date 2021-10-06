# -*- coding: utf8 -*-

# 가변 매개변수와 기본 매개변수 활용해보기

import time

# 가변 매개변수로 무한정 받음
def outer(*args):
  # 함수가 실행되는지 확인
  print(args)
  # 외부함수로부터 매개변수 전달받음 / 기본 매개변수 입력
  def inner(value1, value2, n=3):
    # 기본 매개변수의 수만큼 for문을 돌린다.
    for i in range(n):
      # 1초 간격으로 출력하기.
      if i == i :
        time.sleep(1)
      # 외부함수에 들어온 인자값을 내부함수에서 출력한다.
      print(value1, value2)
  # 내부함수로 매개변수 전달
  return inner(*args)

# 함수호출 및 매개변수 전달
outer("Hello", "Python")

def function(value1, value2, *args, valueA=10, valueB=20):
  print(value1, value2)
  print(args)
  print(valueA, valueB)

function(1,2,3,4,5,6,7,8,9,10,valueA=11, valueB=22)
# 예상 출력값 : 1, 2
            #   (3, 4, 5, 6, 7, 8, 9, 10)
            #   (10, 20)