from itertools import combinations, chain
from operator import mul
from functools import reduce


def readints():
    return [int(n) for n in input().split()]


def powerset(xs):
    return list(chain.from_iterable(combinations(xs, n + 1) for n in range(len(xs))))


def product(xs):
    return reduce(mul, xs, 1)


def taste(ingredients):
    Ss, Bs = zip(*ingredients)
    return abs(product(Ss) - sum(Bs))


N = int(input())
ingredients = [readints() for _ in range(N)]

tastes = [*map(taste, powerset(ingredients))]

print(min(tastes))
