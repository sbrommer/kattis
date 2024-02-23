def readints():
    return [int(n) for n in input().split()]


def readint():
    return readints()[0]


n = readint()

for _ in range(n):
    m = readint()
    r = readint()

    cs = [set([i]) for i in range(m)]

    for _ in range(r):
        f, t = readints()
        fs = next(c for c in cs if f in c)
        ts = next(c for c in cs if t in c)
        if fs != ts:
            fs.update(ts)
            cs.remove(ts)

    print(len(cs) - 1)
