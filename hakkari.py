n, m = map(int, input().split())
grid = [[c == '*' for c in input()] for _ in range(n)]

print(sum(ismine for line in grid for ismine in line))

for y, line in enumerate(grid, 1):
    for x, ismine in enumerate(line, 1):
        if ismine:
            print(y, x)
