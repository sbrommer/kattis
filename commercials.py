o = open(0)

N, P = [int(n) for n in o.readline().split()]

cs = [int(n) - P for n in o.readline().split()]

# Kadane's algorithm
max_local = 0
max_global = 0

for i in range(N):
    max_local = max(cs[i], cs[i] + max_local)
    max_global = max(max_global, max_local)

print(max_global)
