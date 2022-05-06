o = open(0)


def readnm():
    return map(int, o.readline().split())


def readcd():
    return int(o.readline())


n, m = readnm()

while (n, m) != (0, 0):
    jack = set(readcd() for _ in range(n))
    jill = set(readcd() for _ in range(m))

    print(len(jack & jill))

    n, m = readnm()
