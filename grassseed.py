import sys

c = float(sys.stdin.readline())
n = int(sys.stdin.readline())

area = 0

for _ in range(n):
    line = sys.stdin.readline()
    (w, l) = list(map(float, line.split()))
    area += w * l

print(area * c)