from heapq import heappop, heappush
from itertools import dropwhile

# Produce primes
primes = list(range(2, 10000))

for i in range(2, 101):
    if i in primes:
        for j in range(2*i, 10000, i):
            if j in primes:
                primes.remove(j)

primes = list(dropwhile(lambda p: p < 1000, primes))


# Create graph
def neighbours(u, v):
    return sum(a != b for a, b in zip(u, v)) == 1


V = [f'{p:04d}' for p in primes]
G = {u: set(v for v in V if neighbours(u, v)) for u in V}


# Dijkstra
def Dijkstra(f, t):
    q = [(0, f)]
    unvisited = set(V)
    prev = {v: None for v in V}

    while q:
        d, u = heappop(q)

        if u in unvisited:
            unvisited.remove(u)

            if u == t:
                return d

            for v in G[u] & unvisited:
                prev[v] = prev[v] or u
                heappush(q, (d+1, v))

    return 'Impossible'


# Solve
T = int(input())

for _ in range(T):
    print(Dijkstra(*input().split()))
