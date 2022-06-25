from math import sqrt
from operator import mul
from functools import reduce

ss = [int(s) for s in input().split()]
t = sum(ss) / 2
a = sqrt(reduce(mul, [t - s for s in ss]))

print(a)
