# -*- coding: utf8 -*-

# map 이란?

# 특정 리스트를 기반으로 새로운 리스트로 만들어주는 기능
# 가상의 공간에 값을 저장한다. (제너레이터 함수)
# 메모리 값을 줄이고 싶으면 map을 사용하고,
# 상관없으면 list 내포함수를 사용한다.

# 제곱을 하는 기능을 만든다.
def squared(value):
  return value * value

# 리스트 생성
a = list(range(int(input("(기존) 숫자를 입력하세요:"))))

# 리스트에 제곱 기능을 사용.
# 기존 값의 제곱 된 리스트가 생성
print(list(map(squared, a)))

print("-" * 50)

# 람다를 사용하면 2줄로 코드를 줄일 수 있다.
b = list(range(int(input("(람다) 숫자를 입력하세요:"))))
print(list(map(lambda number: number * number, b)))

print("-" * 50)

# 리스트내포를 사용하면 람다와 맵을 한꺼번에 사용한 것과 같은 성능.
c = list(range(int(input("(리스트내포)) 숫자를 입력하세요:"))))

# 짝수만 출력한다.
print([i * i for i in c if i % 2 == 0])