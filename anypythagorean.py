n = int(input())


def triple(n):
    for c in range(1, n):
        for b in range(1, c + 1):
            a = n - (b + c)
            if 1 <= a <= b and a**2 + b**2 == c**2:
                return a, b, c

    return 0, 0, 0


print(*triple(n))
