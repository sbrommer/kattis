from statistics import mean


def readints():
    return [int(n) for n in input().split()]


T, = readints()

for _ in range(T):
    input()
    input()

    cs = readints()
    es = readints()

    μc = mean(cs)
    μe = mean(es)

    print(sum(μe < c < μc for c in cs))
