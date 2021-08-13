# -*- coding: utf8 -*-

# 클래스 내에 함수를 만들고,
# 스태틱메소드로 반환값을 함수로 만든다.
# 함수는 가변매개변수로 함수를 짤 것.
# 모든 값은 곱해서 리턴한다.

# 클래스 생성
class mulclass1 :
  # 클래스 내 메소드를 함수 반환을 변경
  @staticmethod
  # 함수생성
  def mul(*args):
    muls = 1
    for i in args:
      muls *= i
    return muls

# 객체 생성
mu = mulclass1

print(mu.mul(5,7,9,10))
