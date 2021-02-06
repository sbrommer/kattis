import sys
from math import sqrt

t = int(sys.stdin.readline())

for _ in range(t):
    m = sys.stdin.readline()[:-1]
    s = int(sqrt(len(m)))

    for c in range(s-1, -1, -1):
        for r in range(0, s):
            print(m[r*s + c], end='')

    print()