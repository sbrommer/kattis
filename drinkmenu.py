from collections import defaultdict

n, m = map(int, input().split())
drinks = [input() for _ in range(n)]
orders = [input() for _ in range(m)]

customers = defaultdict(int)

for o in orders:
    print(drinks[customers[o]])
    customers[o] += 1
