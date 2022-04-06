from math import sqrt

L, R = [int(c) for c in open(0).readline().split()]

R_min = sqrt(2 * (L / 2) ** 2)

print('nope' if R_min > R else 'fits')
