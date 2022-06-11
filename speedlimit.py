o = open(0)

n = int(o.readline())

while n >= 0:
    # parse
    ss, ts = [], []

    for _ in range(n):
        s, t = [int(i) for i in o.readline().split()]
        ss.append(s)
        ts.append(t)

    # calculate distance
    ts = [t2 - t1 for t1, t2 in zip([0] + ts, ts)]
    d = sum(s * t for s, t in zip(ss, ts))

    print(d, 'miles')

    n = int(o.readline())
