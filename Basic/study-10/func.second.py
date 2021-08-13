# -*- coding: utf8 -*-

# start~end 까지 있는 모든 정수를 더하는 함수
def sum_all(start, end):
  value = 0
  # for문의 (1,10)을 매개변수를 이용해서 대입한다.
  for i in range(start, end + 1):
    value += i
  return value
      
print(sum_all(1,10))

print("-" * 30)

def f_1(x):
  return (2 * x) + 1
print(f_1(10))

def f_2(x):
  return (x ** 2) + (2 * x) + 1
print(f_2(10))

print("-" * 30)
