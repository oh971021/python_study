# -*- coding: utf8 -*-

# 팩토리얼이란?
# n! = 1 * 2 * 3 * .... (n-2) * (n-1) * n
# n! = n * (n-1)
# 0! = 1

n = int(input("팩토리얼을 구할 값을 입력하세요 : "))

# 재귀함수
def factorial_2(n):
  if n == 0:
    return 1
  else:
    return n * factorial_2(n-1)

print("재귀함수로 구한 값 : {}".format(factorial_2(n)))
