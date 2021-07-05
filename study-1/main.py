print("Hello, Python")

# 연산 출력해보기
x = tuple([1,2,3])
a, b, c = x
print(a, b, c) 

d = a + b + c
print(d)

# 모듈 별칭 사용하기
import math as m
print(m.pi)

# 연산자 알아보기
aa = 100; bb = 200
print("100, 200에 각 ** 2 연산자 사용 = ", aa ** 2, bb ** 2)

# 자료형의 클래스, 메타 클래스 확인 print 뒤로 하나씩 넣어보면 확인 가능하다.
type(int), type(float), type(complex), type(bool)
type(10), type(10.1), type(10+1), type(True)

print("자료형의 클래스를 확인한다 = ", type(10))

# Type으로 Class를 찍으면 메타클래스가 나온다.
def __init__(self, name) :
    self.name = name
Person = type("Person",(object,),{'__init__' : __init__})
print("클래스의 네임 = ", Person('Jun').name)
print("클래스의 타입 = ", Person)

# 새로운 값을 넣으면 값이 뭉개져서 프린트 된다.
Person = 100
print("새로운 값을 넣으면 = ", Person)

# 객체는 자신을 생성한 클래스 정보를 가지고 있다.
print("10의 클래스 정보 확인하기 = ", (10).__class__.__name__)
print("100.1의 클래스 정보 확인하기 = ", (10.1).__class__.__name__)
print("10+1의 클래스 정보 확인하기 = ", (10+1).__class__.__name__)
print("True의 클래스 정보 확인하기 = ", (True).__class__.__name__)