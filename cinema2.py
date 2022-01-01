# Parse
lines = open(0).readlines()
N = int(lines[0].split()[0])
G = map(int, lines[1].split())

# Solution
r = 0

for g in G:
    N -= int(g)
    r += N < 0

print(r)
