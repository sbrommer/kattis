from sys import stdin

n = int(stdin.readline())
ds = list(map(int, stdin.readline().split()))

print(1, end=' ')

for d in range(n-1):
    print(ds.index(d) + 2, end=' ')