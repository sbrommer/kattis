from math import ceil

# Read input
r = len(input().split())
n = int(input())

kids = [input() for _ in range(n)]

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
