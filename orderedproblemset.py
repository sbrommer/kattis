from more_itertools import chunked

n, *ps = [int(n) for n in open(0).readlines()]


def true_claim(k):
    cs = list(chunked(ps, n // k))
    return all(max(a) < min(b) for a, b in zip(cs, cs[1:]))


ks = [k for k in range(2, n + 1) if not n % k and true_claim(k)]

if ks:
    print(*ks, sep='\n')
else:
    print('-1')
