from collections import defaultdict

trips = defaultdict(list)

n = int(input())
for _ in range(n):
    s, y = input().split()
    trips[s] += [int(y)]

trips = {s: sorted(ys) for s, ys in trips.items()}

q = int(input())
for _ in range(q):
    s, k = input().split()
    print(trips[s][int(k)-1])
