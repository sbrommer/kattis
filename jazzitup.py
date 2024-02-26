from math import sqrt, ceil


def primes(n):
    prime = [True] * n

    for p in range(2, ceil(sqrt(n))):
        if prime[p]:
            for i in range(p ** 2, n, p):
                prime[i] = False

    return [p for p in range(1, n) if prime[p]]


n = int(input())
max_m = ceil(sqrt(10 ** 5))

for m in primes(max_m)[1:]:
    if n % m:
        print(m)
        break
