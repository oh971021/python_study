# -*- coding: utf8 -*-

class OJS :
    def __init__(self, x, y) :
        self.x = x
        self.y = y

o = OJS

# __setattribute__ call (네임스페이스에 새로운 값을 갱신)
print(setattr(o, 'z', 300))
print(o.__dict__)

print(setattr(o, 'y', 200))
print(o.__dict__)

print(setattr(o, 'x', 100))
print(o.__dict__)

#  (클래스 내에 해당 원소가 있는지 확인)
print(hasattr(o, 'x'))

# __getattribute__ call (네임스페이스에 값이 있는지 조회)
print(getattr(o, 'z'))

# __delete__ call (네임스페이스의 값을 삭제)
print(delattr(o, 'z'))

print(hasattr(o, 'z'))
