import sys

ints = list(map(int, sys.stdin.readline().split()))

ints.sort()

print(ints[0] * ints[2])