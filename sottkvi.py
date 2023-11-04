nkd, *ds = open(0).readlines()

n, k, d = map(int, nkd.split())

print(sum(int(di) + 14 <= k + d for di in ds))
