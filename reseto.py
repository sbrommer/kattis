N, K = [int(n) for n in input().split()]

xs = [True, True] + [False] * (N - 1)

while K:
    P = xs.index(False)

    for x in range(P, N + 1, P):
        K -= not xs[x]

        xs[x] = True

        if not K:
            print(x)
            break
