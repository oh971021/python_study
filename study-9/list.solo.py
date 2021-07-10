# 딕셔너리의 값을 리스트 내포형으로 작성해보기

# 딕셔너리의 키, 값 생성
key_list = ["name", "age", "school", "grade"]
value_list = ["오준석", 25, "영진전문대학교", 'A']

# 딕셔너리 생성
Student = {}

# 키와 값을 순서대로 매칭
for i in range(len(key_list)):
  # 딕셔너리에 들어가는 키값은 [](list)로 묶어준다.
  # i의 값을 넣을 때도 리스트, 순서대로 넣는다.
  Student[key_list[i]] = value_list[i]

# 값이 들어간 딕셔너리 출력
print(Student)