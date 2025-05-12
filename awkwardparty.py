n = int(input())
xs = [*map(int, input().split())]
ix = {}
m = n

for i, x in enumerate(xs):
    if x in ix:
        m = min(m, i - ix[x])

    ix[x] = i

print(m)
