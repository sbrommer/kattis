from itertools import accumulate as cumsum
from operator import add

N, H = map(int, input().split())

hs = [[0] * H, [0] * H]

for n in range(N):
    h = int(input())

    hs[n % 2][h - 1] += 1

hs[0] = cumsum(hs[0][::-1])
hs[1] = cumsum(hs[1][::-1])

smashes = [*map(add, hs[0], [*hs[1]][::-1])]

best = min(smashes)
print(best, smashes.count(best))
