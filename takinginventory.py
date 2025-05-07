from collections import defaultdict

storage = defaultdict(int)

n = int(input())
for _ in range(n):
    s, c = input().split()
    storage[s] += int(c)

for s in storage:
    d, m = divmod(storage[s], 64)
    storage[s] = d + bool(m)

for s, c in storage.items():
    print(s, c)
