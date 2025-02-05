N = int(input())
days = [input() for _ in range(N)]

print([*zip(days, days[1:])].count(('drunk', 'sober')))
