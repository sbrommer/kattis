# Import.
from collections import defaultdict

# Read and parse data.
o = open(0)
N, M = list(map(int, o.readline().split()))

# Parse friendships
fs = defaultdict(lambda: 0)
for _ in range(M):
	i, j = list(map(int, o.readline().split()))
	fs[i] += 1
	fs[j] += 1

# Calculate score
for Sf in range(1, N + 1):
	Pf = fs[Sf]
	print(Pf - Sf, end=' ')
