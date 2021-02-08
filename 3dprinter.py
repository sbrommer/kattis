from sys import stdin
from math import log2, ceil

n = int(stdin.readline())

print(ceil(log2(n))+1)
