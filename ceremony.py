from collections import Counter

n = int(input())
hs = Counter(map(int, input().split()))

best = n
floors = 0

for h in sorted(hs):
    floors += hs[h]
    best = min(best, h + n - floors)

print(best)
