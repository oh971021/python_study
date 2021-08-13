# -*- coding: utf8 -*-
# import datetime 공부

import datetime
now = datetime.datetime.now()

if 3 <= now.month <= 5 :
  print("이번달은 {}월로 봄이다.".format(now.month))
elif 3 <= now.month <= 5 :
  print("이번달은 {}월로 여름이다.".format(now.month))
elif 3 <= now.month <= 5 :
  print("이번달은 {}월로 가을이다.".format(now.month))
else:
  print("이번달은 {}월로 겨울이다.".format(now.month))  


print("-" * 50)

user = float(input("학점을 입력하세요\n"))

# 위에서 비교한 값은 더이상 쓰이지 않기 떄문에 밑에서는 바깥 비교는 하지 않아도 된다.
if 4.5 <4.= user :
  print("신")
elif 4.2 < user :
  print("교수님의 사랑")
elif 3.5 < user :
  print("현 체제의 수호자")
elif 2.8 < user :
  print("일반인")
elif 2.3 < user :
  print("일탈을 꿈꾸는 소시민")
elif 1.75 < user :
  print("오락문화의 선구자")
elif 1.0 < user :
  print("불가촉천민")
elif 0.5 < user :
  print("자벌레")
elif 0 < user :
  print("플랑크톤")
else :
  print("시대를 앞서가는 혁명의 씨앗")     