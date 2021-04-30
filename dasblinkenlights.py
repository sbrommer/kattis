from sys import stdin

p, q, s = list(map(int, stdin.readline().split()))

ps = set(range(p,s+1,p))
qs = set(range(q,s+1,q))

print('yes' if ps.intersection(qs) else 'no')
