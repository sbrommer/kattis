def readints():
    return tuple(map(int, input().split()))


N, M = readints()

V = list(range(N))

adj = [set() for _ in range(N)]
for _ in range(M):
    u, v = readints()
    adj[u] |= {v}
    adj[v] |= {u}


def bipartite(V, adj):
    colour = [None] * N
    q = []

    for u in V:
        if colour[u] is None:
            colour[u] = True
            q += [u]

        while q:
            v, *q = q
            for w in adj[v]:
                if colour[w] is None:
                    colour[w] = not colour[v]
                    q += [w]
                elif colour[v] == colour[w]:
                    return False

    return True


print('attend here' if bipartite(V, adj) else 'no way')
