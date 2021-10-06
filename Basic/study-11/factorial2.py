# -*- coding: utf8 -*-

# 팩토리얼 복습

# 팩토리얼이란?
# n! = 1 * 2 * 3 * .... (n-2) * (n-1) * n
# n! = n * (n-1)
# 0! = 1

fac = int(input(">> 팩토리얼을 구할 숫자를 입력하세요 : "))
# 초기값을 설정한다.
result = 1

# for문으로 fac+1의 갯수까지 돌리는데 
# 한번 돌릴때마다 result에 i의 값을 넣어준다. 
for i in range(1, fac+1, 1):
  result *= i
  print("{}".format(i),end=" * ")

print()
print(result)