# -*- coding: utf8 -*-

def alert_start(func):
  def new_func(*args, **kwargs):
    print("함수가 시작됩니다")
    return func(*args, **kwargs)
  return new_func

print(alert_start(print)("파이썬"))

def alert_end(func):
  def new_func(*args, **kwargs):
    result = func(*args,**kwargs)
    print("함수가 끝났습니다.")
    return result
  return new_func

print(alert_end(print)("프로그래밍"))

@alert_start
def add(x, y):
  return x + y

print(add(1, 3))