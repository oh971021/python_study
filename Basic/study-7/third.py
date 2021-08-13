# -*- coding: utf8 -*-
# 숫자 맞추기 게임
import random

n = random.randint(1,50)

while True :
    r = int(input("1~50 사이의 숫자를 입력하세요 >>"))
    if n > r :
        print("{}보다 큰수 입니다.".format(r))
    else :
        print("{}보다 작은수 입니다.".format(r))
    if n == r :
        print("정답을 맟추셨습니다.")
        break