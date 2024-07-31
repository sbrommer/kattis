from collections import defaultdict
from heapq import heappush, heappop


def readints():
    return [int(n) for n in input().split()]


n, m = readints()
V = set(range(1, n+1))
E = dict()
neighbours = defaultdict(set)

for _ in range(m):
    a, b, c = readints()
    E[(a, b)] = c
    E[(b, a)] = c
    neighbours[a].add(b)
    neighbours[b].add(a)


# Dijkstra
q = [(0, 1)]  # (distance, node)
unvisited = set(V)

d, u = heappop(q)
while u != n:
    if u in unvisited:
        unvisited.remove(u)
        for v in [b for a, b in E if a == u]:
            if v in unvisited:
                heappush(q, (d + E[(u, v)], v))
    d, u = heappop(q)

print(d)
