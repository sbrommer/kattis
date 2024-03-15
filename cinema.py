def readints():
    return [int(n) for n in input().split()]


N, _ = readints()
groups = readints()

angry = 0

while N and groups:
    g, *groups = groups
    if N < g:
        angry += 1
    else:
        N -= g

print(angry + len(groups))
