from statistics import mean

o = open(0)


def readints():
    return [int(n) for n in o.readline().split()]


T, = readints()

for _ in range(T):
    for _ in range(2):
        o.readline()

    cs = readints()
    es = readints()

    print(sum(mean(es) < c < mean(cs) for c in cs))
