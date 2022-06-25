def readints():
    return [int(n) for n in input().split()]


s, t, n = readints()
ds = readints()
bs = readints()
cs = readints()

for i in range(n):
    s += ds[i]
    if s % cs[i] != 0:
        s += cs[i] - (s % cs[i])
    s += bs[i]

s += ds[-1]

print('yes' if s <= t else 'no')
