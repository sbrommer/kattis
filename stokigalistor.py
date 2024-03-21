from operator import ne
from itertools import starmap

input()

l = [int(n) for n in input().split()]

print(sum(starmap(ne, zip(l, sorted(l)))))
