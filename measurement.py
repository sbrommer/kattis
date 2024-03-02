from operator import mul
from functools import reduce

units = ['league', 'mile', 'furlong', 'chain',
         'yard', 'foot', 'inch', 'thou']

abbrs = ['lea', 'mi', 'fur', 'ch', 'yd', 'ft', 'in', 'th']

conversion = [3, 8, 10, 22, 3, 12, 1000]


def get_index(u):
    return units.index(u) if u in units else abbrs.index(u)


def product(xs):
    return reduce(mul, xs, 1)


v, u, _, w = input().split()

i_u = get_index(u)
i_w = get_index(w)
v = int(v)

if i_u < i_w:
    print(v * product(conversion[i_u: i_w]))
else:
    print(v / product(conversion[i_w: i_u]))
