# -*- coding: utf8 -*-
# 랜덤모듈을 사용한 확률문 만들기

import random

ran = random.randint(0,50)
if ran % 2 == 0 :
    print("그냥 집에간다")
else :
    print("복권을 산다")
    for i in range(0, 2):
        LottoNumbers = random.sample(range(1, 50),6)
        i = LottoNumbers
        print(i)