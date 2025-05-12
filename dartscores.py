from math import hypot


def readints():
    return map(int, input().split())


T, = readints()

for _ in range(T):
    n, = readints()
    points = 0
    for _ in range(n):
        d = hypot(*readints())
        for p in range(11)[::-1]:
            if d <= 20 * (11 - p):
                break
        points += p
    print(points)
