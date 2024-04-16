def base10(B, X):
    if B == 1 and all(x == '1' for x in X):
        return len(X)

    try:
        return int(X, B)
    except ValueError:
        return None


N = int(input())

for _ in range(N):
    X, op, Y, _, Z = input().split()

    valid = ''

    for B in range(1, 37):
        ns = [base10(B, n) for n in [X, Y, Z]]
        x, y, z = ns

        # checks: valid base + within limits + valid expression
        if all(ns) and \
           all(1 <= n <= 2**32-1 for n in ns) and \
           eval(f'{x}{op}{y}=={z}'):
            valid += '_123456789abcdefghijklmnopqrstuvwxyz0'[B]

    print(valid if valid else 'invalid')
