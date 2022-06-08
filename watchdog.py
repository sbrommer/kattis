from math import sqrt

o = open(0)


def readints():
    return [int(n) for n in o.readline().split()]


def dist(X1, Y1, X2, Y2):
    return sqrt((X2 - X1) ** 2 + (Y2 - Y1) ** 2)


def leash(hs, S):
    for X in range(S):
        for Y in range(S):
            if [X, Y] not in hs:
                d_edge = min(X, Y, S - X, S - Y)
                d_hatch = max(dist(X, Y, *h) for h in hs)

                if d_hatch <= d_edge:
                    return X, Y

    return -1, -1


N = int(o.readline())

for _ in range(N):
    S, H = readints()
    hs = [readints() for _ in range(H)]

    X, Y = leash(hs, S)

    if X >= 0:
        print(X, Y)
    else:
        print('poodle')
