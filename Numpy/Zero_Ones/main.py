import numpy as np

a = np.zeros((2,2))
print(a)

b = np.ones((2,2))
print(b)

c = np.ones((5,5))
d = (c != 0)
c[1:4,1:4] = 0
print(c)
print(d)

e = d[d>-1]

print(e)