import sys

n = int(sys.stdin.readline())

qaly = 0

for _ in range(n):
    line = sys.stdin.readline()
    (q, y) = list(map(float, line.split()))
    qaly += q * y

print(qaly)
