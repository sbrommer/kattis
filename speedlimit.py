o = open(0)

n = int(o.readline())

while n >= 0:
    # parse
    inp = [map(int, o.readline().split()) for _ in range(n)]
    ss, ts = map(list, zip(*inp))

    # calculate distance
    ts = [t2 - t1 for t1, t2 in zip([0] + ts, ts)]
    d = sum(s * t for s, t in zip(ss, ts))

    print(d, 'miles')

    n = int(o.readline())
