from math import sqrt

x, y, x1, y1, x2, y2 = map(int, input().split())

dx = max(x1 - x, x - x2, 0)
dy = max(y1 - y, y - y2, 0)

print(sqrt(dx ** 2 + dy ** 2))
