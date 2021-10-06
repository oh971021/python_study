# -*- coding: utf8 -*-
# 문자열.함수(매개변수, 매개변수)
# = 주어 동사 ( 목적어 목적어 )

print("{}년 {}월 {}일 {}요일".format(1997, 10, 21, "화"))

# Upper : 대문자로 / Lower : 소문자로

print("Hello".upper())
print("HELLO".lower())

# strip : 양쪽의 공백을 제거해주는 함수

print("  묹자   ".strip())
print("  묹자   ".lstrip()) # 왼쪽 공백 제거
print("  묹자   ".rstrip()) # 오른쪽 공백 제거

# find : 몇번 째에 있는지 찾는 함수 ( 왼쪽부터 )
# rfind : 같은값이 있을 때 오른쪽에서 부터 찾는다.

print("가나다라라라라마바사라라".find("라")) 
print("가나다라라라라마바사라라".rfind("라")) 

# in : 문자열 사이에 찾고자하는 문자가 있으면 true 없으면 false

print("가나" in "가나다라마바사")
print("아자차카" in "가나다라마바사")

# split : 띄워쓰기로 잘라서 (list형태로) 표시한다.

print("10 20 30 40 50".split(" "))

# 함수와 파괴적 함수

string = "hello"
string.upper() # 함수는 원본을 변경 시키지않는다.
print("일호점 : ", string) # 그래서 여기선 원본이 출력된다.
print("이호점 : ", string.upper()) 