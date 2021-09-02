from sys import stdin

def readints():
    return list(map(int, stdin.readline().split()))

input = readints()

while len(input) > 0:
    M, P, L, E, R, S, N = input

    for _ in range(N):
        C = P // S
        P = L // R
        L = M * E
        M = C

    print(M)

    input = readints()
