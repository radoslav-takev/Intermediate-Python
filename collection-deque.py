import collections
from collections import deque

d = deque("hello")
print(d)
d.append('4')
d.append(5)
print(d)
d.appendleft(3)
print(d)
d.clear()
print(d)
