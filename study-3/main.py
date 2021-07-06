a = input("첫번째 숫자를 입력해주세요 ")
b = input("두번째 숫자를 입력해주세요 ")
print(a, b)
# swap
c = b
b = a
a = c
print(a,b)
a, b = b, a
print(a,b)

# input(">>> ") # 함수