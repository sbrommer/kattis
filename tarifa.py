import sys

x = int(sys.stdin.readline())
n = int(sys.stdin.readline())

total = x * (n + 1)

for _ in range(n):
    p = int(sys.stdin.readline())
    total -= p

print(total)
