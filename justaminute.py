from sys import stdin

N = int(stdin.readline())

m = 0
s = 0

for _ in range(N):
    M, S = list(map(int, stdin.readline().split()))
    m += M
    s += S

sl_minute = s / (60 * m)

print(sl_minute if sl_minute > 1 else 'measurement error')
