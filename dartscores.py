from math import hypot


def readints():
    return map(int, input().split())


T, = readints()

for _ in range(T):
    n, = readints()
    points = 0
    for _ in range(n):
        d = hypot(*readints())
        p = 0
        for p in range(10):
            if p <= 10 - d / 20:
                p += 1
            else:
                break
        points += p
    print(points)
