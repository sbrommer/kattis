from math import sqrt
from itertools import permutations

o = open(0)


def readpoint():
    return [int(n) for n in o.readline().split()]


def d(p1, p2):
    return sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)


def f(ps):
    return d(ps[0], ps[1]) + d(ps[0], ps[2])


def p4(m, l, r):
    return l[0] + r[0] - m[0], l[1] + r[1] - m[1]


ps = [readpoint() for _ in range(3)]
ps = min(permutations(ps), key=f)

print(*map(int, p4(*ps)))
