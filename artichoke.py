from math import sin, cos
from itertools import accumulate

p, a, b, c, d, n = [int(i) for i in input().split()]


def price(k):
    return p * (sin(a * k + b) + cos(c * k + d) + 2)


prices = [price(k) for k in range(1, n+1)]
maxs = list(accumulate(prices, max))
mins = list(accumulate(prices[::-1], min))[::-1]
declines = [mx - mn for mx, mn in zip(maxs, mins)]
print(max(declines))
