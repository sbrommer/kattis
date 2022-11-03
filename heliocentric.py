o = open(0)


def readints():
    return list(map(int, o.readline().split()))


inp = readints()
c = 1

while len(inp) > 0:
    e, m = inp
    d = 0

    while e % 365 != m % 687:
        e += 1
        m += 1
        d += 1

    print('Case', c, end='')
    print(':', d)

    c += 1
    inp = readints()
