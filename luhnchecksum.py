T = int(input())

for _ in range(T):
    n = list(map(int, input()))

    for i in range(len(n)):
        if not (i + len(n)) % 2:
            n[i] *= 2
            n[i] = sum(divmod(n[i], 10))

    print('FAIL' if sum(n) % 10 else 'PASS')
