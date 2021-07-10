# 피보나치 수열?
# 등장배경 : 토끼가 어떤 속도로 번식을 할까?

# f(n) = f(n-1) + f(n-2)

# 나뭇가지 갯수, 꽃잎 갯수를 구할 수 있다.

import time

counter = 0

start_time_1 = time.time()

def f(n):
  # 전역변수를 함수 내에서 사용할 때 글로벌 키워드로 변수를 지정한다.
  global counter
  # 계산 할때마다 카운터가 올라간다.
  counter += 1
  # 피보나치 수열 1과 2는 1이기 때문에 1로 지정한다.
  if n == 1 or n == 2:
    return 1
  else:
    return f(n-1) + f(n-2)

print("재귀함수")
# 재귀함수의 문제 : 수가 커지면 계산이 너무 느리다.
print(f(35))
# 피보나치 수열의 계산 수를 확인하는 카운터
print("{}번 계산을 했습니다.".format(counter))
# 계산하는데 걸린 시간
print(time.time() - start_time_1)
print("-" * 30)

# 재귀함수의 계산이 오래걸리는 문제를 메모화를 통해 해결한다.
# 메모화 (메모장에 적어놓고 가져와서 사용하는 느낌)
memo = {1: 1, 2: 1}
start_time_2 = time.time()
def f(n):
  if n in memo :
    return memo[n]
  output = f(n-1) + f(n-2)
  memo[n] = output
  return output

print("메모화")
print(f(10))
print(time.time() - start_time_2)