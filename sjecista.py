from sys import stdin

n = int(stdin.readline())

print(n * (n-1) * (n-2) * (n-3) // 24)
