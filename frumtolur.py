# not correct, but good enough for the first 100 primes
def sieve():
    primes = [0, 0] + [1] * 600

    for p in range(2, 600):
        if primes[p]:
            yield p
            for q in range(2 * p, 600, p):
                primes[q] = False


generator = sieve()
for _ in range(100):
    print(next(generator))
