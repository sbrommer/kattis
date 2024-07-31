def readints():
    return [int(n) for n in input().split()]


N, M = readints()
A, B, K, G = readints()
gs = readints()
streets = {}

for _ in range(M):
    a, b, L = readints()
    streets[(a, b)] = L
    streets[(b, a)] = L


def wheres_george_at(t):
    route = list(zip(gs, gs[1:]))
    T0 = 0
    for i in route:
        T1 = T0 + streets[i]
        if T0 <= t < T1:
            return i, T1 - t
        T0 = T1
    return None, 0


def time(u, v, t):
    if (u, v) not in streets:
        return float('inf')

    g_loc, delta = wheres_george_at(t)

    return streets[(u, v)] + (g_loc in [(u, v), (v, u)]) * delta


# Dijkstra
unvisited = set(range(1, N + 1))
ds = {n: 0 if n == A else float('inf') for n in unvisited}

while unvisited:
    u = min(unvisited, key=ds.get)
    unvisited.remove(u)
    for v in unvisited:
        d_uv = time(u, v, ds[u] + K)
        ds[v] = min(ds[u] + d_uv, ds[v])

print(ds[B])
