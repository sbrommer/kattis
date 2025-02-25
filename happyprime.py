def prime(m):
    if m <= 1:
        return False
    for d in range(2, int(m**0.5)+1):
        if not m % d:
            return False
    return True


def happy(m):
    seen = set()
    while m not in seen:
        seen |= {m}
        m = sum(int(d) ** 2 for d in str(m))

        if m == 1:
            return True

    return False


P = int(input())

for _ in range(P):
    K, m = map(int, input().split())

    print(K, m, 'YES' if happy(m) and prime(m) else 'NO')
