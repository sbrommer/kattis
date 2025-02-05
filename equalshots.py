def readints():
    return map(int, input().split())


def get_alcohol(n):
    V, C = 0, 0

    for _ in range(n):
        v, c = readints()
        V += v
        C += v * c

    return V, C


a, b = readints()

Va, Ca = get_alcohol(a)
Vb, Cb = get_alcohol(b)

print('same' if Va * Cb == Vb * Ca else 'different')
