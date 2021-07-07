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