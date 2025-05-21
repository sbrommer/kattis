from collections import deque

n, m = map(int, input().split())
goal = (n-1, m-1)

grid = {(x, y): int(d)
        for x in range(n)
        for y, d in enumerate(input())}

visited = [[0] * m for _ in range(n)]
visited[0][0] = 1

q = deque([(0, 0, 0)])

while q:
    x, y, s = q.popleft()

    if (x, y) == goal:
        break

    d = grid[x, y]
    for x, y in [(x+d, y), (x-d, y), (x, y-d), (x, y+d)]:
        if (x, y) in grid and not visited[x][y]:
            visited[x][y] = 1
            q.append((x, y, s+1))

print(s if (x, y) == goal else -1)
