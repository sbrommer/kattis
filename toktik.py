from collections import defaultdict

total = defaultdict(int)

n = int(input())

for _ in range(n):
    toktikker, views = input().split()
    views = int(views)

    total[toktikker] += views

print(max(total, key=total.get))
