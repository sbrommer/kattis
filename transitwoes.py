from sys import stdin

(s, t, n) = list(map(int, stdin.readline().split()))
ds = list(map(int, stdin.readline().split()))
bs = list(map(int, stdin.readline().split()))
cs = list(map(int, stdin.readline().split()))

for i in range(n):
    s += ds[i]
    if s % cs[i] != 0:
        s += cs[i] - (s % cs[i])
    s += bs[i]

s += ds[-1]

print('yes' if s <= t else 'no')
