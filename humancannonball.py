from math import sqrt


def parse_input():
    def readfloats():
        return [float(i) for i in input().split()]

    a = readfloats()
    b = readfloats()

    n = int(input())
    cannons = [readfloats() for _ in range(n)]

    return [a] + cannons + [b]


def get_time(u, v, cannon):
    d = sqrt((u[0] - v[0]) ** 2 + (u[1] - v[1]) ** 2)
    t_run = d / 5
    t_cannon = 2 + abs(d - 50) / 5
    return min(t_run, t_cannon) if cannon else t_run


def Dijkstra(G):
    unvisited = set(range(len(G)))
    ds = {n: 0 if n == 0 else float('inf') for n in unvisited}

    while unvisited:
        u = min(unvisited, key=ds.get)
        unvisited.remove(u)

        for v in unvisited:
            ds[v] = min(ds[u] + G[u][v], ds[v])

    return ds


V = parse_input()

G = [[get_time(u, v, u not in [V[0], V[-1]]) for v in V] for u in V]

print(Dijkstra(G)[len(V) - 1])
