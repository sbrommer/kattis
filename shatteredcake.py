from operator import mul


def readints():
    return [int(n) for n in input().split()]


W, = readints()
N, = readints()

A = sum(mul(*readints()) for _ in range(N))

print(A // W)
