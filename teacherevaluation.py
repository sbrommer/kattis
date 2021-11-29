from sys import stdin
from math import ceil

def readints():
    return list(map(int, stdin.readline().split()))

N, P = readints()
S = sum(readints())

print('impossible' if P == 100 else ceil((S - P * N) / (P - 100)))
