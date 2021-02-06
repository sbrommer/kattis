import sys

line = sys.stdin.readline()

(r1, s) = list(map(int, line.split()))

r2 = 2*s - r1

print(r2)
