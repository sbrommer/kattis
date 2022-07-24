from math import sqrt

# read pattern
ix = [None] * 9

for i in range(3):
    row = [int(n) for n in input().split()]
    for j in range(3):
        ix[row[j] - 1] = (i, j)

# calculate distance
l = 0

for i in range(8):
    n1, n2 = ix[i], ix[i+1]

    dx = n2[0] - n1[0]
    dy = n2[1] - n1[1]

    l += sqrt(dx ** 2 + dy ** 2)

print(l)
