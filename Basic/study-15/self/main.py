class Func :
  def func1(f) :
    print("function1")
  def func2(self):
    print("function2")

  # 클래스 내에 정의 된 self 는 클래스 인스턴스다.
  def func3(self) :
    print(id(self))

f = Func()

print(f.func1())
print(f.func2())
print(f.func3(), id(f))

f2 = Func()

# f2 라는 인스턴스를 생성한다.
print(Func.func2(f2))

