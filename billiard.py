from sys import stdin
from math import sqrt, atan, degrees

def readints():
    return list(map(int, stdin.readline().split()))

input = readints()

while sum(input) > 0:
    a, b, s, m, n = input

    d_h = a * m
    d_v = b * n
    A = 90 - degrees(atan(d_h / d_v))

    d = sqrt(d_h ** 2 + d_v ** 2)
    v = d / s

    print("%.2f" % A, "%.2f" % v)

    input = readints()
