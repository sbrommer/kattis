from sys import stdin

n, m = list(map(int, stdin.readline().split()))

lists = []

for _ in range(n):
    lists.append(set(stdin.readline().split()))

same = list(set.intersection(*lists))
same.sort()

print(len(same))
for item in same:
    print(item)
