from sys import stdin
from math import ceil

B, Br, Bs, A, As = list(map(int, stdin.readline().split()))

m = (Br - B) * Bs
print(A + int(m / As) + 1)
