from itertools import accumulate, starmap
from operator import gt, sub, add


def v(s):
    return 0 if s == ' ' else ord(s) - ord('a') + 1


def vi(u):
    return ' ' if not u else chr(ord('a') + u - 1)


def encrypt(xs):
    xs = map(v, xs)  # step 1
    xs = accumulate(xs)  # step 2
    xs = [x % 27 for x in xs]  # step 3
    return ''.join(map(vi, xs))  # step 4


def decrypt(xs):
    xs = list(map(v, xs))  # step 4 inverse
    ms = accumulate([gt(*t) * 27 for t in zip([0] + xs, xs)])  # step 3 inverse
    xs = list(starmap(add, zip(xs, ms)))
    xs = list(starmap(sub, zip(xs, [0] + xs)))  # step 2 inverse
    return ''.join(map(vi, xs))  # step 1 inverse


n = int(input())
for i in range(n):
    e, ss = input().split(' ', 1)

    print(encrypt(ss) if e == 'e' else decrypt(ss))
