# -*- coding: utf8 -*-
# 랜덤모듈을 사용한 확률문 만들기

import random as rd

ran = rd.randint(0,1)
if ran % 2 == 0 :
    print("안먹는다.")
else :
    print("먹는다.")