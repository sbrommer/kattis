from sys import stdin

(n, l) = list(map(int, stdin.readline().split()))

t = 0
d_prev = 0

for _ in range(n):
    (d, r, g) = list(map(int, stdin.readline().split()))

    t += d - d_prev
    d_prev = d
    t_green = t - (t % (r + g)) + r
    t = max(t, t_green)

t += l - d_prev

print(t)
