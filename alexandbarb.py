from functools import cache

k, m, n = map(int, input().split())

print('Alex' if m <= k % (m+n) else 'Barb')
