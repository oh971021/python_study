# -*- coding: utf8 -*-
for i in range(1, 10, 1) :
  print("-" * 2, "{}".format(i),"단", "-" * 2)
  for j in range(1, 10, 1) :
    if j == 5 :
      pass
    else : 
      print("{} * {} = {}".format(i, j, i*j))
