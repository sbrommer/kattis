from sys import stdin
from collections import defaultdict

R, S, K = list(map(int, stdin.readline().split()))

window = []
rackets = defaultdict(lambda: 0)

for r_fly in range(R):
    line = stdin.readline().strip()
    window.append(list(line))

    for s_fly in range(S):
        if line[s_fly] == '*':
            for dr in range(1, K-1):
                for ds in range(1, K-1):
                    r = r_fly - dr
                    s = s_fly - ds

                    if 0 <= r <= R-K and 0 <= s <= S-K:
                        rackets[(r, s)] += 1

(r_best, s_best), n = max(rackets.items(), key=lambda elem: elem[1])

print(n)

for r in [r_best, r_best+K-1]:
    for s in [s_best, s_best+K-1]:
        window[r][s] = '+'

for r in [r_best, r_best+K-1]:
    for s in range(s_best+1, s_best+K-1):
        window[r][s] = '-'

for s in [s_best, s_best+K-1]:
    for r in range(r_best+1, r_best+K-1):
        window[r][s] = '|'

for r in range(R):
    print(*window[r], sep='')
