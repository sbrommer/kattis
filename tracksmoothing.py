from math import sqrt, pi


def readints():
    return [int(x) for x in input().split()]


def distance(coords):
    p, q = coords
    return sqrt((q[0] - p[0]) ** 2 + (q[1] - p[1]) ** 2)


t = readints()[0]

for _ in range(t):
    r, n = readints()

    coords = [readints() for _ in range(n)]
    straights = zip(coords, coords[1:] + [coords[0]])

    dist_old = sum(map(distance, straights))
    dist_new = dist_old - 2 * pi * r
    factor = dist_new / dist_old

    print(factor if factor > 0 else 'Not possible')
