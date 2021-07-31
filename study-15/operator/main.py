class Person :
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __eq__(self, other) :
    print("eq() 함수")
    return (self.age == other.age)
  def __ne__(self, other) :
    print("ne() 함수")
    return self.age != other.age
  def __gt__(self, other) :
    print("gt() 함수")
    return self.age > other.age
  def __ge__(self, other) :
    print("ge() 함수")
    return self.age >= other.age
  def __lt__(self, other) :
    print("lt() 함수")
    return self.age < other.age
  def __le__(self, other) :
    print("le() 함수")
    return self.age <= other.age
  
p = Person("준석", 25)
print(p == p)
print(p != p)
print(p > p)
print(p >= p)
print(p < p)
print(p <= p)
