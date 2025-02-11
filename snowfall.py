n = int(input())

snow = 0

for _ in range(n):
    t, a = map(int, input().split())
    snow = max(snow + [1, -1][t] * a, 0)

print(snow)
