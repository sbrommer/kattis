from sys import stdin
from math import ceil

# Read input
r = len(stdin.readline().split())
n = int(stdin.readline())

kids = []
for _ in range(n):
    kids.append(stdin.readline().strip())

# Select teams - print green right away,
# print blue later.
print(ceil(n / 2))

i = 0
blues = []
while kids:
    i = (i + r - 1) % len(kids)

    kid = kids[i]
    del kids[i]

    if (len(kids) - n) % 2:
        print(kid)
    else:
        blues.append(kid)

print(len(blues), *blues, sep='\n')
