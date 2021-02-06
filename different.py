import sys

lines = sys.stdin.readlines()

for line in lines:
    (x1, x2) = list(map(int, line.split()))
    print(abs(x1 - x2))
