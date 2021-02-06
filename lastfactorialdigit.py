import sys
from math import factorial

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    f = factorial(n)
    print(f % 10)