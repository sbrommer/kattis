from math import sqrt

L, R = map(int, input().split())

print('nope' if sqrt(2 * (L / 2) ** 2) > R else 'fits')
