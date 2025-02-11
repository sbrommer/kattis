n, r, c = map(int, input().split())

rows = [input().split() for _ in range(r)]
attendance = [input() for _ in range(n)]

for y in range(r):
    print('left' if rows[y][0] == attendance[y * c] else 'right')
