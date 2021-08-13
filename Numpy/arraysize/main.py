"""""
 == 다차원 배열 구조 ==
- 넘파이의 다차원 배열은 ndarray 클래스에 의해 만들어지는 객체다.
- 이 클래스의 특징은 1차원 데이터를 관리하는데,
- 이 1차원 데이터를 메타정보를 이용해서 다양한 차원 데이터 튜플을 보여준다.
- 데이터를 관리하는 영역과 메타정보를 관리하는 영역을 분리해서 보다 신속하게 계산을 처리한다.

"""""

import numpy as np

a = np.arange(1,13).reshape(2,3,2)

print("a : {}".format(a))
print("\n")
print("a는 {}차원 배열이다.".format(a.ndim))
print("a안에 있는 원소의 타입은 {}이다.".format(a.dtype))
print("a의 배열의 크기는 {}이다.".format(a.size))
print("a가 가진 원소 하나의 크기는 {}이다.".format(a.itemsize))