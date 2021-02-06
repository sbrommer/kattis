import sys

n = int(sys.stdin.readline())

for _ in range(n):
    k, *os = list(map(int, sys.stdin.readline().split()))
    print(1 + sum(os) - k)