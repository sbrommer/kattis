# Parse
o = open(0)

N, T = [int(n) for n in o.readline().split()]
ts = [int(o.readline()) for _ in range(N)]

# Calculate
ts.sort(reverse=True)
ts_start = range(0, len(ts) * T, T)
ts_end = [t + s for t, s in zip(ts, ts_start)]

print('YES' if all(t > (len(ts) - 1) * T for t in ts_end) else 'NO')
