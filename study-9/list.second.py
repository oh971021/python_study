# 1~100 사이의 수를 2진수로 변환 했을 때, 
# 0 이 하나만 포함된 숫자를 찾고,
# 그 숫자의 합을 더하는 예제
output = 0
for i in range(0, 100 + 1):
  if "{:b}".format(i).count("0") == 1:
    print("{}의 2진수 변환 값은 : {:b}".format(i,i))
    output += i
print("합계 : {}".format(output))

# 위으 코드를 리스트 내포형으로 작성하면 코드가 짧아진다.
output = [i for i in range(0, 100 + 1) if "{:b}".format(i).count("0") == 1]
print("합계 : {}".format(sum(output)))