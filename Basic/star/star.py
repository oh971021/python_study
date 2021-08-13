a = int(input("정수를 입력하세요 : "))


for i in range(a):
    for k in range(a,i,-1):
        print(' ',end='')
    for j in range((i+1)*2-1):
        print("*",end='')
    print()

