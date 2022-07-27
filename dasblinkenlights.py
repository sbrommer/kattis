p, q, s = map(int, input().split())

ps = set(range(p, s + 1, p))
qs = set(range(q, s + 1, q))

print('yes' if ps.intersection(qs) else 'no')
