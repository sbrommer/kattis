n = int(input())
ds = list(map(int, input().split()))

print(1, *[ds.index(d) + 2 for d in range(n-1)])
