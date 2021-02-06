import sys

max_i = 0
max_s = 0

for i in range(1, 6):
    line = sys.stdin.readline()
    s = sum(map(int, line.split()))
    if s > max_s:
        max_i = i
        max_s = s

print(max_i, max_s)
