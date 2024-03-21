from operator import mul
from itertools import starmap, accumulate

primes = [1, 2, 3, 5, 7, 11, 13, 17, 19]


def to_number(vs):
    decimals = list(accumulate(primes, mul))
    return sum(starmap(mul, zip(vs, decimals)))


overflow = to_number([p - 1 for p in primes[1:]])
vs = [int(n) for n in input().split()]

print(overflow - to_number(vs))
