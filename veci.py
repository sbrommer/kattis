from itertools import permutations

X = input()
xs = tuple(map(int, X))

bigger = set()
for p in permutations(xs):
    if p > xs:
        bigger.add(p)

print(0 if not bigger else ''.join(map(str, min(bigger))))
