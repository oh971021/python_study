from _typeshed import WriteableBuffer


class Animal :
  def eat(self,obj) :
    self.obj = obj

class Person(Animal) :
  pass

class Person_(Animal) :
  def eat(self,obj) :
    #super().eat(obj)
    self.sss = obj

%%Writefile sleep.py
def sleep(obj, value) :
  return obj.sleep(value)

%%Writefile eat.py
def eat(obj, value) :
  return obj.eat(value)

# go 인터페이스 o ==> py 인터페이스 x : 대신 함수처리해서 데코해서 사용한다.
# 클래스는 함수의 행동을 제약한다.
import eat
import sleep
# 파이썬은 함수를 만들어서 그 함수를 import해서 사용한다.

p = Person()

eat.eat(p,"먹을것")

print(p.__dict__)