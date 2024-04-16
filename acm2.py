from itertools import accumulate, takewhile


def readints():
    return [int(n) for n in input().split()]


T = 300
N, p = readints()
ts = readints()

ts = [ts[p]] + sorted(ts[:p] + ts[p+1:])
solve_times = list(takewhile(lambda t: t <= 300, accumulate(ts)))

print(len(solve_times), sum(solve_times))
