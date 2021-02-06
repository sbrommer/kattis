import sys

line = sys.stdin.readline()
(a, i) = map(int, line.split())

print(a * (i-1) + 1)
