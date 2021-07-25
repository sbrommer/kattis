from sys import stdin

n, k = map(int, stdin.readline().split())

r = 0
for _ in range(k):
    r += int(stdin.readline().strip())

min = (r - (n - k) * 3) / n
max = (r + (n - k) * 3) / n

print(min, max)
