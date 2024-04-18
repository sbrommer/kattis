def readints():
    return [int(n) for n in input().split()]


N, = readints()
E, = readints()

songs = [set() for _ in range(N+1)]

for e in range(E):
    vs = readints()[1:]

    if 1 in vs:
        for v in vs:
            songs[v] |= {e}

    else:
        known = set.union(*[songs[v] for v in vs])
        for v in vs:
            songs[v] |= known

print(*[i for i, s in enumerate(songs) if s == songs[1]], sep='\n')
