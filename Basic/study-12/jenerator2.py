# 제너레이터?

# 이터레이터를 직접 만들 때 사용하는 기능
# 함수 내부에 yield 라는 키워드가 포함되는 것으로 구분한다.
# 일회용 함수다.

# yield = 양보하다, 먼저 가게 하다.

def func() :
  print("A")
  yield 100 # next 한번은 여기서 멈춤.
  print("B")  
  yield 200
  print("C")
  yield 300
  print("D")
  yield 400
  print("E")
  yield 500

jen = func()

"""""
value = next(jen)
value = next(jen)
value = next(jen)
value = next(jen)
value = next(jen)
# 일드 5번인데 6번을 넥스트로 출력하면 이터레이터 에러발생
# value = next(jen)

"""""

# for 반복문과 조합해서 많이 사용한다.
for i in jen:
  print(i)

