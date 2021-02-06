from sys import stdin
from math import sqrt

(ss) = list(map(int, stdin.readline().split()))

s = sum(ss) / 2
a = sqrt((s-ss[0]) * (s-ss[1]) * (s-ss[2]) * (s-ss[3]))

print(a)
