from sys import stdin

a, b = map(int, stdin.readline().split())

print(min(a, b), max(a, b))
