ii = [
  [5,6,7,8],
  [9,10,11],
  [12,13],
  [14]
]

print(ii)

for i in ii :
  for j in i :
    print(j)

ii = ii[0] + ii[1] + ii[2] + ii[3]

for i in ii :
  print(i)

jj = [1,2,3,4]

# 순환문으로 만드는 iter 명령어
j = iter(jj)

# next(인자)를 써줌으로써 순환문의 순서가 돌아가는 기능
print(next(j), next(j), next(j), next(j))

def add(x,y) :
  print (y + x)

add(ii, jj)