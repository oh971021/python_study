import numpy as np
import operator as op

"""""
# Universal 함수
 - 다차원 배열의 원소가 많기 때문에 각 원소별로 계산하려면 순환문을 작성해야 하지만
 - Numpy Universal 함수는 기본으로 벡터화 연산을 지원하므로 순환문없이 모든 원소와 계산이 가능하다.
 - 결론 : 순환문 없이 모든 원소들을 순환하면서 처리하는 함수
 - 쉽게말하면 연산 기능을 가진 함수( 예를들어 add, mul 등등 )를 Universal함수라고 하는 듯하다.

"""""

# Universal 함수에는 어떤게 있는지 확인해봅시다.

count = 0

for i, v in np.__dict__.items() :
    if type(v) == np.ufunc :
        print(i, end=", ")
        count += 1
    
print("\n")

a = np.arange(5)

print("배열에서 사용하는 것을 보기위해 배열 생성 : ", a)
print("a[1] + a[1] = ", op.add(1,1))
print("a[i] + a[i] = ", op.add(a,a))