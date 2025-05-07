def readints():
    return [*map(int, input().split())]


N, Q = readints()

groupsize = [1] * (N+1)
leaders = [n for n in range(N+1)]


def find(a):
    if leaders[a] != a:
        leaders[a] = find(leaders[a])

    return leaders[a]


def unite(a, b):
    a, b = find(a), find(b)
    if a != b:
        groupsize[a] += groupsize[b]
        leaders[b] = a


for _ in range(Q):
    t, *q = readints()

    match t:
        case 1:
            unite(*q)

        case 2:
            print(groupsize[find(*q)] - 1)
