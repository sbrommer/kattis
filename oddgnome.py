def readints():
    return list(map(int, input().split()))


def getking(ints):
    g, *gnomes = ints

    for i in range(g):
        if gnomes[i] + 1 != gnomes[i + 1]:
            return i + 2


n, = readints()

print(*[getking(readints()) for _ in range(n)])
