
# 클래스라는 이름의 클래스는 object 클래스를 상속받는다.
class Klass(object):
  # 정보를 입력하는 기능을 넣어줌.
  def set_info(self, name, age) :
    self.name = name
    self.age = age

  # 프린트를 하는 기능을 넣어줌.
  def print_name(self) :
    print("이름 : ", self.name)
    print("나이 : ", self.age)

# a라는 객체 생성
a = Klass()

# 그 객체의 클래스에서 타고 들어가서 기능을 사용함.
a.set_info("준석", 25)

print(a.__dict__)
print(a.name)

print()

a1 = Klass()
a1.set_info("석준", 52)

print(a1)
a1.print_name()

print(id(a), id(a1))