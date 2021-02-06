import sys

line = sys.stdin.readline()

(n, h, v) = list(map(int, line.split()))

print(max(h, n-h) * max(v, n-v) * 4)
