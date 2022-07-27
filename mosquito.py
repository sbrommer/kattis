o = open(0)


def readints():
    return list(map(int, open(0).readline().split()))


i = readints()

while len(i) > 0:
    M, P, L, E, R, S, N = i

    for _ in range(N):
        C = P // S
        P = L // R
        L = M * E
        M = C

    print(M)

    i = readints()
