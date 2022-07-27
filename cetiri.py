ns = list(map(int, input().split()))

ns.sort()

d1 = ns[1] - ns[0]
d2 = ns[2] - ns[1]

if d1 < d2:
    print(ns[1] + d1)
elif d1 > d2:
    print(ns[0] + d2)
else:
    print(ns[2] + d1)
