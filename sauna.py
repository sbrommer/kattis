N = int(input())
temps = [(int(t) for t in input().split()) for _ in range(N)]
mins, maxs = [*zip(*temps)]

mn, mx = max(mins), min(maxs)

print('bad news' if mx < mn else f'{mx - mn + 1} {mn}')
