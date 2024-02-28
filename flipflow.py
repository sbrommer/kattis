from functools import reduce


def readints():
    return [int(n) for n in input().split()]


t, s, _ = readints()
A = [0] + readints() + [t]
deltas = [b - a for a, b in zip(A, A[1:])]

top = reduce(lambda top, delta: s - max(top - delta, 0), deltas, 0)

print(s - top)
