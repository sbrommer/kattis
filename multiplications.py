from operator import mul
from functools import reduce

N = int(input())
a = [int(input()) for _ in range(N)]

print(reduce(mul, a, 1) % (10**9+7))
