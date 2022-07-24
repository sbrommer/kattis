L, H = map(int, input().split())

n = 0

for c in range(L, H + 1):
    ds = list(map(int, str(c)))
    n += len(set(ds)) == len(ds) and \
         all(map(lambda d: d and not c % d, ds))

print(n)
