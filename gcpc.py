def readints():
    return map(int, input().split())


def better(i, j):
    return A[i] > A[j] or (A[i] == A[j] and B[i] < B[j])


n, m = readints()
A = [0] * (n+1)
B = [0] * (n+1)
above = set()

for _ in range(m):
    t, p = readints()
    A[t] += 1
    B[t] += p

    if better(t, 1):
        above |= {t}

    if t == 1:
        rem = set()
        for a in above:
            if not better(a, 1):
                rem |= {a}
        above -= rem

    print(len(above) + 1)
