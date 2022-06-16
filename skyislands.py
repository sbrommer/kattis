# Parse
o = open(0)


def readints():
    return [int(n) for n in o.readline().split()]


N, M = readints()

graph = {n: set() for n in range(1, N + 1)}

for _ in range(M):
    a, b = readints()
    graph[a].add(b)
    graph[b].add(a)

# DFS
vs = [1]
q = [1]

while q:
    a = q.pop()
    for b in graph[a]:
        if b not in vs:
            vs.append(b)
            q.append(b)

# Result
print('YES' if len(vs) == N else 'NO')
