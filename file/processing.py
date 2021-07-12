"""""
특정 대상()
- 텍스트 파일 : 텍스트에디터로 열 수 있다. (비주얼 스튜디오 코드 = 텍스트 에디터)
- 바이너리 파일 : 텍스트에디터로 열 수 없다. (이미지, 동영상, 워드, 엑셀, PDF 등)

어떻게 다룰 것인가()
- 쓰기
  - 새로(write) : w
  - 있는 파일 뒤에(append) : a
- 읽기(read) : r

"""""

# close를 포함한 기능 whit open
with open("test.txt", "a") as file:
  file.write("안녕하세요")

# 파일을 여는 함수 open
# file 객체 생성 ( 새로만든 파일 w )
# 운영체제에 따라 글자가 깨질 수 있는데, 인코딩 형태를 강제로 변경해서 컴파일되게 만든다. 
file = open("test.txt", "w")
file.write("오늘은 파일처리법에 대해서 공부합니다.")
# file을 모두 사용하고 닫아준다. ( 닫아주지 않으면 충돌이 생긴다 )
file.close()

# file 객체 생성 ( 읽기파일 r )
file = open("test.txt", "r")
print(file.read())
file.close()

