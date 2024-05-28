from functools import reduce
from operator import mul

def readints():
    return map(int, input().split())


n, V = readints()

print(max(reduce(mul, readints()) - V for _ in range(n)))
