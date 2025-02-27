from bisect import bisect_left


def readints():
    return [int(n) for n in input().split()]


s, p, m, n = readints()
ts = readints()

mem = [0] * (n+1)

for i in range(n)[::-1]:
    mem[i] = min(s + mem[i+1],
                 p + mem[bisect_left(ts, ts[i]+m, i)])

print(mem[0])
