import sys

n = int(sys.stdin.readline())

x = 0

for _ in range(n):
    p = int(sys.stdin.readline())
    number = p // 10
    power  = p % 10
    x += number ** power

print(x)
