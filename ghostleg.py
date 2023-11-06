n, m = map(int, input().split())

p = list(range(1, n + 1))

for _ in range(m):
    a = int(input())
    p[a - 1], p[a] = p[a], p[a - 1]

print('\n'.join(map(str, p)))
