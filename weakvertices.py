def get_graph():
    return {v1: set(v2
                    for v2, e in enumerate(input().split())
                    if int(e))
            for v1 in range(n)}


def get_weak(graph):
    weak = set(range(len(graph)))

    for v1 in range(len(graph)):
        for v2 in graph[v1]:
            if graph[v1].intersection(graph[v2]):
                weak.remove(v1)
                break

    return weak


n = int(input())
while n >= 0:
    print(*sorted(get_weak(get_graph())))
    n = int(input())
