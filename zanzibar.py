T = int(input())

for _ in range(T):
    ts = [int(t) for t in input().split()]

    bs = [max(0, t2 - t1 * 2) for t1, t2 in zip(ts, ts[1:])]

    print(sum(bs))
