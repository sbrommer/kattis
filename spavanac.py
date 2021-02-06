import sys

line = sys.stdin.readline()
(h, m) = map(int, line.split())

dh = m < 45

h = (h - dh) % 24
m = (m - 45) % 60

print(h, m)
