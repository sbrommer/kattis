from sys import stdin

n = int(stdin.readline())
ts = list(map(int, stdin.readline().split()))
max_ts = list(map(max, zip(ts, ts[2:])))

max_t = min(max_ts)

print(max_ts.index(max_t) + 1, max_t)
