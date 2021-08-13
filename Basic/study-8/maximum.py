# 변수 할당 (객체 생성)
max_value = 0
a = 0
b = 0

# for문으로 1 ~ 99 값 구하기
# i = 1로 시작해서 100까지 도는데, j = 100 - i 값을 출력한다.
for i in range(1, 99 +1):
  j = 100 - i
  print(i, "*", j, "=", i * j)

  #최댓값 구하기
  # max_value에 할당되는 값이 i*j보다 작은 경우
  # max , a , b 변수에 각각 값을 할당한다.
  if max_value < i * j :
    max_value = i * j
    a = i
    b = j

# 최대가 되는 값을 출력한다.
print("최대가 되는 경우 = {} * {} = {}".format(a,b,max_value))