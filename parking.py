from sys import stdin

costs = [0] + list(map(int, stdin.readline().split()))

trucks = []

for _ in range(3):
    trucks.append(list(map(int, stdin.readline().split())))

t_end = max(trucks, key=lambda t : t[1])[1]
cost = 0

for t in range(1, t_end+1):
    n = sum(list(map(lambda r : t in range(*r), trucks)))
    cost += costs[n] * n

print(cost)
