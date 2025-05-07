def readints():
    return [*map(int, input().split())]


def d(p, q):
    return ((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2) ** 0.5


bed = readints()
n, = readints()
monsters = [readints() for _ in range(n)]

safe = all(d(bed, monster) > 8 for monster in monsters)

print('YES' if safe else 'NO')
