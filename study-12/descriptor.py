# -*- coding: utf8 -*-

# 디스크립터 구현

# 갱신가능한 디스크립터 생성
class MutableAttribute:
    def __init__(self, value=None):
        self.value = value
    def __get__(self, instance, owner):
        return self.value
    def __set__(self, instance, value):
        self.value = value
    def __delete__(self, instance):
        del self.value

# 갱신불가능한 디스크립터 생성
class ImmutableAttribute:
    def __init__(self, func):
        self.func = func
    def __get__(self, instance, owner):
        return self.func(instance)
    def __set__(self, instance, value):
        raise AttributeError("Read Only")
    def __delete__(self, instance):
        raise AttributeError("Read Only")

# 메인 클래스 정의 : 메소드는 불가변적 처리
class Circle:
    pi = 3.14
    radius = MutableAttribute(10)
    diameter = ImmutableAttribute(lambda self: self.radius * 2)

    @ImmutableAttribute
    def circumference(self):
        return self.radius * self.pu * 2

    @ImmutableAttribute
    def area(self):
        return self.radius ** 2 * 2

c = Circle()

print(c.radius.__dict__)
print(c.area.__dict__)
print(c.diameter.__dict__)

try :
    c.area = 123
except Exception as e :
    print(e)