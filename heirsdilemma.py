from sys import stdin

L, H = list(map(int, stdin.readline().split()))

n = 0

for c in range(L, H + 1):
    ds = list(map(int, str(c)))
    if len(set(ds)) == len(ds) and \
       all(map(lambda d : d and not c % d, ds)):
        n += 1

print(n)
