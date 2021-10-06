# # 스네이크 케이스
# i_love_you : 기본적 사용

# # 캐멀 케이스
# ILoveYou : 클래스 이름 (앞글자가 대문자)

# 클래스 (틀) : 학생은 이름이라는 속성을 갖고 있어.
# 객체 (실체화) : 학생 이름은 "오준석"이다
# 실체화 한 객체 = "인스턴스"

# __로 실행되는 함수들은 어떠한 경우에 자동으로 실행되는 친구들
class Student :

  # 요 친구는 내부에서 어떠한 자료형을 문자열로 바꿔서 사용해주는 메소드
  def __str__(self):
    return "제 이름은 {}, {}살 입니다".format(self.name, self.age)

  def __init__(self, name, age) :
    print("객체가 생성됩니다.")
    self.name = name
    self.age = age
  
  # 프로그램이 종료 되기 전 메모리 정리하면서
  # 선언 된 객체도 소멸 되는데, 이때 소멸자 메소드가 실행된다.
  def __del__(self) :
    print("객체가 사라집니다.")

  def 출력(self) :
    print(self.name, self.age)

student = Student("오준석", 25)
student.출력()
print(student)