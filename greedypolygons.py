from sys import stdin
from math import pi, tan, degrees

def readints():
    return list(map(int, stdin.readline().split()))

N = int(stdin.readline())

for _ in range(N):
    n, l, d, g = readints()

    p = n * l
    a = l / (2 * tan(180 / degrees(n)))
    r = d * g

    A = 0.5 * p * a

    A += n * r * l
    A += pi * r ** 2

    print(A)