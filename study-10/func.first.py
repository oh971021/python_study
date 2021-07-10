# -*- coding: utf8 -*-

def print_n_times(value, n):
  for i in range(n):
    print(value)

# print_n_times("반가워요") # 매개변수의 수가 적으면 타입에러
print_n_times("안녕하세요", 2)
# print_n_times("안녕히가세요", 10) # 매개변수의 수가 많아도 타입에러

print("-" * 30)

#가변 매개변수
def Func(value1, value2, *args):
  print(value1)
  print(value2)
  print(args)

Func(0, 1, 2, 3, 4, 5, 6, 7, "Hello", "Python")

print("-" * 30)

# 기본 매개변수 (디폴트 매개변수) 
def print_n_times(value, n=5):
  for i in range(n):
    print(value)

print_n_times("안녕하세요")