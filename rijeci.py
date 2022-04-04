from sys import stdin

k = int(stdin.readline())

a, b = 1, 0

for _ in range(k):
    a, b = b, a + b

print(a, b)