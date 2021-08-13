# -*- coding: utf8 -*-

# 프로퍼티 처리하기.

class OJS :
    # 초기화 값 할당
    def __init__(self) :
        self._name = 5
    # Getter
    @property
    def name(self) :
        return self._name
    # Setter , value값을 넣어줘야 하기 때문에 인자에 value 추가
    @name.setter
    def name(self, value) :
        # _name 의 값을 갱신한다.
        self._name = value

o = OJS()
print("현재 초기화 값 : {}".format(o.name))
o.name = (int(input("변경할 값을 적어주세요 : ")))
print("변경 된 값 : {}".format(o.name))