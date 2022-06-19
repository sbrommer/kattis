from re import finditer

# Read input
o = open(0)

N1, N2 = [int(n) for n in o.readline().split()]
l = o.readline().strip()
r = o.readline().strip()
T = int(o.readline())

# Initialise values
ants = list(l[::-1] + r)
dirs = ['>'] * N1 + ['<'] * N2

# Walk the ants
for _ in range(T):
    for i in finditer('><', ''.join(dirs)):
        i = i.start()
        ants[i], ants[i+1] = ants[i+1], ants[i]
        dirs[i], dirs[i+1] = '<', '>'

# Result
print(''.join(ants))
