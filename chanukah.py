import sys

p = int(sys.stdin.readline())

for _ in range(p):
    (k, n) = list(map(int, sys.stdin.readline().split()))
    print(k, sum(range(2, n+2)))