from sys import stdin
import math

n = int(stdin.readline())

for _ in range(n):
    m = int(stdin.readline())

    x, y, th = 0, 0, 0

    for i in range(m):
        a, d = list(map(float, stdin.readline().split()))

        th -= math.radians(a)
        x += math.sin(th) * d
        y += math.cos(th) * d

    print(x, y)
