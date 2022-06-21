def readints():
    return [int(n) for n in input().split()]


def T(a, b, c):
    return c + b ** 2 / (4 * a)


t, = readints()

for _ in range(t):
    n, = readints()

    print(max(range(n), key=lambda _: T(*readints())) + 1)
