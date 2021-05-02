from sys import stdin
from itertools import permutations

X = stdin.readline().strip()
xs = tuple(map(int, X))

bigger = set()
for p in permutations(xs):
    if p > xs:
        bigger.add(p)

print(0 if not bigger else ''.join(map(str, min(bigger))))
