x, y = [int(c) for c in input().split()]
n = int(input())

for _ in range(n):
    l, u, f = [float(c) for c in input().split()]
    y -= (u - l) * (1 - f)

print(x / y)
