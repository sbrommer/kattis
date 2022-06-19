o = open(0)


def readints():
    return [int(n) for n in o.readline().split()]


N = readints()[0]
ps = sorted([readints() for _ in range(N)])


floor = [0] * 10000
l = 0
for Y, X1, X2 in ps:
    l += 2 * Y - floor[X1] - floor[X2 - 1]

    for x in range(X1, X2):
        floor[x] = Y

print(l)
