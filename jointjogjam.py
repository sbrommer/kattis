from sys import stdin
from math import sqrt

[ksx, ksy, osx, osy, kex, key, oex, oey] =\
    list(map(int, stdin.readline().split()))

ds = sqrt((osx - ksx) ** 2 + (osy - ksy) ** 2)
de = sqrt((oex - kex) ** 2 + (oey - key) ** 2)

print(max(ds, de))
