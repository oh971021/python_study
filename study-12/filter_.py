# -*- coding: utf8 -*-

# filter란 ?

# filter(func, iterable) : 리스트 등에서 필터링을 해준다.

"""""
def even(value):
  return value % 2 ==0
"""""

# 100이라는 리스트를 만든다.
a = list(range(100))

# 위의 함수 코딩과 같은 기능을 한다.
# 람다는 일회용 함수다.
# 람다를 변수에 할당하면 여러번 사용할 수 있다.
even = lambda number: number % 2 == 0

# 0~ 100 까지 짝수만 출력한다.
b = filter(even, a)
print(list(b))
