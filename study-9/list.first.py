# -*- coding: utf8 -*-

# 리스트 객체 생성
array = []

# 2씩 증가하는 i를 for문으로 돌리고, 
# array 리스트에 i를 넣는다.
# 예상 출력 값 = i의 제곱근
#for i in range(0, 20, 2):
#  array.append(i * i)

# 리스트 내포
array =[i * i for i in range(0,20,2)]
print(array)

print("------")

# 리스트 내포 코딩예제
# for 문을 나열해서 사용하는 것 같다.
# for 문 뒤에 if 를 쓰는 것도 가능하다.
array_1 = [i for i in range(10) if i % 3 == 0]
array_2 = [i for i in range(0,10,2)]
array_3 = [i for i in range(10)]

print(array_1)
# 예상 출력값 : 0,1,2,3,4,5,6,7,8,9
print(array_2)
# 예상 출력값 : 0,2,4,6,8
print(array_3)
# 예상 출력값 == array_1