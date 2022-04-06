o = open(0)

def readints():
    return [int(c) for c in o.readline().split()]


n, k = readints()
xs = readints()

print(*[x for x in xs[k-1::k]])
