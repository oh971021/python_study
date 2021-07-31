# 빈 셀에 변수를 할당하면 이 변수는 전역 변수가 된다.
global_var = "전역변수입니다"

class Klass :
  # 클래스를 정의할 때 클래스 내에서 정의 된 변수를 클래스 속성이라고 한다.
  class_attr = "클래스 속성입니다"

  def __init__(self, in_attr) :
    # self 를 이용해 정의 된 변수를 객체 속성이라고 한다.
    self.instance_attr = in_attr

  def getG(self) :
    # 전역변수는 어디서든 사용 가능하다.
    return global_var

  def getC(self) :
    return type(self).class_attr

  # 객체속성에 접근한다.
  def getI(self) :
    return self.instance_attr


a = Klass("안녕하셔요")

# 클래스속성은 클래스 이름으로 접근한다.
print(Klass.class_attr)

print(a.getG())

print(a.getC())

# 객체 속성은 객체 이름으로 접근한다.
print(a.getI())