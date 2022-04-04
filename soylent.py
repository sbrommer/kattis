from sys import stdin
from math import ceil

def readint():
    return int(stdin.readline())

t = readint()

for _ in range(t):
    n = readint()
    print(ceil(n / 400))
