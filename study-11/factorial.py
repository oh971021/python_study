# 팩토리얼이란?
# n! = 1 * 2 * 3 * .... (n-2) * (n-1) * n
# n! = n * (n-1)
# 0! = 1

print("-- 팩토리얼 --")

def factorial_1(n):
  value = 1
  for i in range(1, n + 1):
    value *= i
  return value

# 재귀함수
def factorial_2(n):
  if n == 0:
    return 1
  else:
    return n * factorial_2(n-1)

print(factorial_1(5))
print(factorial_1(10))

print("-" * 14)
