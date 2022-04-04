from sys import stdin

def readints():
    return list(map(int, stdin.readline().split()))

N, Q = readints()

Xs = readints()

for _ in range(Q):
    r, *line = readints()
    if r == 1:
        (C, X) = line
        Xs[C-1] = X
    if r == 2:
        (A, B) = line
        print(abs(Xs[B-1] - Xs[A-1]))