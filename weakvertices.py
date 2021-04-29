from sys import stdin

def make_graph():
    graph = {}

    for v1 in range(n):
        row = list(map(int, stdin.readline().split()))

        adj = set()

        for v2 in range(n):
            if row[v2]:
                adj.add(v2)

        graph[v1] = adj

    return graph

def get_weak(graph):
    n = len(graph)

    weak = set(range(n))

    for v1 in range(n):
        is_weak = True
        for v2 in graph[v1]:
            if graph[v1].intersection(graph[v2]):
                weak.remove(v1)
                break

    return weak

n = int(stdin.readline())

while  n >= 0:
    graph = make_graph()
    weak = get_weak(graph)

    weak = list(weak)
    weak.sort()

    for v in weak:
        print(v, end=' ')
    print()

    n = int(stdin.readline())


