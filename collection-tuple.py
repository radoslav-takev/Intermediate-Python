# named tuple

import collections
from collections import namedtuple

Point = namedtuple('Point', 'x gy z')

newP = Point(3, 4, 5)
print(newP)