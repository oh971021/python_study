# -*- coding: utf8 -*-

n = int(input("(기존) 몇번 입력할까요? : "))

def call_10_times(func):
  for i in range(n):
    # 콜백함수 (callback)
    func(i)

def print_hello(number):
  print("{}번 입력합니다.".format(n), number)

call_10_times(print_hello)

print("-" * 50)

# 위와 같은 코드는 람다 함수를 통해 print_hello를 만들 수 있다.
x = int(input("(람다) 몇번 입력할까요? : "))

def call_10_times2(func):
  for i in range(x):
    # 콜백함수 (callback)
    func(i)

# 람다는 return을 자동으로 부여해준다.
call_10_times2(lambda number: print("{}번 입력합니다.".format(x), number))