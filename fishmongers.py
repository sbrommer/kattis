def readints():
    return [*map(int, input().split())]


n, m = readints()
fish = sorted(readints(), reverse=True)
mongers = sorted([readints() for _ in range(m)], key=lambda t: -t[1])


def sell(fish, mongers):
    monies = 0
    i = 0

    for x, p in mongers:
        for _ in range(x):
            if i == len(fish):
                return monies

            monies += fish[i] * p
            i += 1

    return monies


print(sell(fish, mongers))
