n = int(input())

colours = [input().lower() for _ in range(n)]
s = sum('pink' in c or 'rose' in c for c in colours)

print(s if s else 'I must watch Star Wars with my daughter')
