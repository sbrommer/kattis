from sys import stdin

x, y = list(map(int, stdin.readline().split()))
r = int(stdin.readline())

print(x - r, y - r)
print(x - r, y + r)
print(x + r, y + r)
print(x + r, y - r)
