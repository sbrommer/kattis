def readints():
    return [int(n) for n in input().split()]


n, m = readints()
grid = [readints() for _ in range(n)]

print(min(sum((abs(r1 - r2) + abs(c1 - c2)) * grid[r2][c2]
              for r2 in range(n)
              for c2 in range(m))
          for r1 in range(n)
          for c1 in range(m)))
