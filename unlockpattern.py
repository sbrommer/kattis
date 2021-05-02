from sys import stdin
from math import sqrt

ix = 9 * [(0,0)]

for i in range(3):
    row = list(map(int, stdin.readline().split()))
    for j in range(3):
        ix[row[j] - 1] = (i, j)

l = 0

for i in range(len(ix) - 1):
    n1, n2 = ix[i], ix[i+1]

    dx = n2[0] - n1[0]
    dy = n2[1] - n1[1]

    l += sqrt(dx ** 2 + dy ** 2)

print(l)
