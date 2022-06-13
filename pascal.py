from math import sqrt


def highest_divisor(N):
    for i in range(2, int(sqrt(N)) + 1):
        d, m = divmod(N, i)
        if not m:
            return d
    return 1


N = int(open(0).readline())

print(N - highest_divisor(N))
