def readints():
    return [int(n) for n in input().split()]


M, N = readints()
U, L, R, D = readints()

frame = [input() for _ in range(M)]

for h in range(U + M + D):
    for w in range(L + N + R):
        if U <= h < U + M and L <= w < L + N:
            print(frame[h - U][w - L], end='')
        else:
            print('#' if h % 2 == w % 2 else '.', end='')
    print()
