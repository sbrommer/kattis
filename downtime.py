from heapq import heappush, heappop
from math import ceil

n, k = map(int, input().split())
ts = [(int(input()), True) for _ in range(n)]

rmax, r = 0, 0

while ts:
    t, e = heappop(ts)
    if e:
        r += 1
        heappush(ts, (t + 1000, False))
    else:
        r -= 1
    rmax = max(rmax, r)

print(ceil(rmax / k))
