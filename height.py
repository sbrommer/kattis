def readints():
    return [int(n) for n in input().split()]


P = readints()[0]

for _ in range(P):
    K, *hs = readints()
    line = set()
    steps = 0

    while hs:
        h, *hs = hs
        steps += sum(l > h for l in line)
        line.add(h)

    print(K, steps)
