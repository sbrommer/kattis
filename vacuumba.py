from math import radians, sin, cos

n = int(input())

for _ in range(n):
    m = int(input())

    x, y, th = 0, 0, 0

    for i in range(m):
        a, d = map(float, input().split())

        th -= radians(a)
        x += sin(th) * d
        y += cos(th) * d

    print(x, y)
