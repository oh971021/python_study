"""""
연산자들의 속도차이를 보기위한 예제.

앞서 말했던 가장 빠른 연산자는 그냥 +,- 이대로 사용하는 것.

"""""
import math
import numpy as np
import operator as op
import timeit


def test1():
    return np.multiply(204614306831, 5291450912850) 

def test2():
    return op.mul(204614306831, 5291450912850)

def test3():
    return 204614306831 * 5291450912850

def test4():
    return (204614306831).__mul__(5291450912850)

t1 = timeit.timeit('test1()', setup='from __main__ import test1', number=100000)
t2 = timeit.timeit('test2()', setup='from __main__ import test2', number=100000)
t3 = timeit.timeit('test3()', setup='from __main__ import test3', number=100000)
t4 = timeit.timeit('test4()', setup='from __main__ import test4', number=100000)

print("np 모듈 사용 : ", t1,"초")
print("op 모듈 사용 : ", t2,"초")
# 이 친구가 가장 빠른 것을 확인 할 수 있다.
print("빌트인 op 사용 : ", t3,"초")
print("빌트인 __op__ 사용 : ", t4,"초")