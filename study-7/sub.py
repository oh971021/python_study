# 만들어 볼 거 : 외부함수, 내부함수 참조 하는 로직 짜보기
# 복습내용 : 데코레이터 사용해보기, 외부함수, 내부함수 사용하면서 글로벌변수, 지역변수 사용해보기.
Globals1 = int(input("첫 번째 글로벌 변수로 쓸만한 정수를 입력해주세요 : "))
Globals2 = int(input("두 번째 글로벌 변수로 쓸만한 정수를 입력해주세요 : "))

def add(x, y) :
  return x+y

def outer(*args) :
  global Globals1

  print("outer 실행")
  print(Globals1)
  
  locals = "나는야 로컬변수"

  def inner(*args) :
    nonlocal locals

    print("inner 실행")
    print(locals)
    print("값은? : ", args)

    return args
  
  return inner(*args)

outer(Globals1, Globals2)

print(add(Globals1, Globals2))
