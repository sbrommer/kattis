input()
M = int(input())
problems = input().split()

points = [[int(p) for p in input().split()]
          for _ in range(M)]

points = [*map(sum, zip(*points))]

print(problems[points.index(max(points))])
