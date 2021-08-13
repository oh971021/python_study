# -*- coding: utf8 -*-

# 함수선언
def flatten(data):
  # 평탄화 시킨 데이터를 넣을 리스트 선언
  output = []

  # 재귀함수를 통해 매개변수로 들어오는 원소를 돌린다.
  for item in data:
    # item의 타입이 list라면 output리스트에 원소를 넣는다.
    if type(item) == list:
      output += flatten(item)
    else:
      # output.append(item)
      output += [item]
  # 원소가 들어간 output을 리턴한다.
  return output

# example 리스트를 flatten 함수로 보냈다가 output으로 리턴받는다.
example = [[1,2,3], [4,[5,6]], 7, [8,9]]
print("원본 : ", example)
print("변환 : ", flatten(example))