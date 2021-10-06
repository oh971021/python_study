# f(n) = f(n-2) + f(n-1)

n = int(input("피보나치 수열을 구할 값을 넣으세요 : "))

def fibonacci(n):
  if n <= 2 :
    return 1
  else :
    return fibonacci(n-2) + fibonacci(n-1)

print(fibonacci(n))