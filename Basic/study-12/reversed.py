# reversed() ?

# 일회용 함수 : 객체로 할당하고 여러번 사용해도 한번만 사용 가능하다.
# 메모리 절약 : 기존 값이 복제가 되는 것이 아니라 기존 값을 거꾸로 출력하기 때문이다.

# reversed 함수 구현
def reversal(list):
  for i in range(len(list)):
    yield list[-i - 1]

# 함수호출 객체 할당 : 리스트가 복제 되지는 않는다.
jenerator = reversal([1,2,3,4,5])

# 기존 메모리의 리스트 값을 거꾸로 출력하는 것
for i in jenerator:
  print(i) 