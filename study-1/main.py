# 파이썬 기능 공부

###################################  day-1 ########################################

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
print("100, 200에 각 ** 2 연산자 사용 = ", aa ** 2, bb ** 2) # aa, bb의 2승을 의미한다.

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


###################################  day-2 ########################################

# 리터럴 표기법 (변수를 선엄함과 동시에 그 값을 지정해주는 표기법)
print("리터럴 표기법 = ", float(100), complex(100), int(100.1))

# 진수 변환 ( 0b = 2진수 , 0o = 8진수 , 0x = 16진수)
print("2진수 =", 0b0001,", 8진수 =", 0o00010, ", 16진수 =", 0x00010 )

# 클래스 지정 및 네임스페이스 확인
class Junseok__ :
    pass # 클래스 초기화 하는 값
J = Junseok__()
J.O = 100
print("O of class of Junseok = ", J.O)
print("Junseok의 네임스페이스 확인 = ", J.__dict__) # 네임스페이스 확인하기 ( 식별자 -> 이름 -> 변수, 함수, 클래스, 모듈, 패키지명 )

# 열(sequence)의 특징 : 하나의 집합에 자료형을 지정해주는데, 그 이유는 같은 타입의 원소만 넣을 수 있기 때문이다.
# 리스트(List)의 특징 : 최상위 클래스 Object로 정의한 리스트에는 단일 클래스가 되기 때문에 아무거나 다 들어올 수 있다. (시퀀스 타입이 될 수 있다.)

# 문자처리 함수
print("가를 아스키코드로 변환하고, 16진법으로 나타내면 = ", hex(ord("가")))
# 한글은 초성 중성 종성으로 이뤄져 있어서 3byte로 나타난다.
print("가를 byte로 나타내보면 = ", "가".encode())
# 그걸 다시 디코딩 해보면
print("다시 decoding 하면 = ", "가".encode().decode())

# list와 tuple 리터럴 표기법
[1,2,3]; (1,2,3)
print("[]의 타입은 = ", type([1,2,3]), "()의 타입은 = ", type((1,2,3)))

v = [1,2,3]
print("list v의 값은?")
for i in range(3) :
    print(v[i])

