n = int(input())
ds = [int(input()) for _ in range(n)]

print(sum(d % 2 for d in ds))
