def mean(xs):
    return sum(xs) // len(xs)


ALs = list(map(int, input().split()))
N, KWF = map(int, input().split())

As = ALs[0::2]
Ls = ALs[1::2]

Ks = [A * L for A, L in zip(As, Ls)]

print(mean(Ks) * N // KWF)
