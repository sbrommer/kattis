from math import hypot


def readints():
    return [int(n) for n in input().split()]


cx, cy, n = readints()
devices = [readints() for _ in range(n)]

maxradii = sorted([hypot(cx-x, cy-y) - r for x, y, r in devices])

print(int(max(0, maxradii[2])))
