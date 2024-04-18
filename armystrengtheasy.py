def readints():
    return [int(n) for n in input().split()]


T, = readints()

for _ in range(T):
    input()
    input()
    G = sorted(readints(), reverse=True)
    M = sorted(readints(), reverse=True)

    while G and M:
        g, m = G[0], M[0]
        w = min(g, m)

        if m == w:
            M.pop()

        elif g == w:
            G.pop()

    print('Godzilla' if G else 'MechaGodzilla')
