from sys import stdin

s = stdin.readline().strip()

n_odd = 0
for c in set(s):
    n_odd += s.count(c) % 2

print(max(0, n_odd - 1))
