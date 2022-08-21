r, c = map(int, input().split())

surface = [input() for _ in range(r)]
visited = set()


def dfs(x, y):
    if (x, y) not in visited:
        visited.add((x, y))
        neighbours = [(x+dx, y+dy)
                      for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]
                      if 0 <= x+dx < c and 0 <= y+dy < r and surface[y+dy][x+dx] in 'LC']
        for nb in neighbours:
            dfs(*nb)


n = 0
for x in range(c):
    for y in range(r):
        if surface[y][x] == 'L' and (x, y) not in visited:
            n += 1
            dfs(x, y)

print(n)
