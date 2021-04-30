from sys import stdin

l, n = list(map(int, stdin.readline().split()))
k = 1

while l % n != 0:
    k += 1
    n -= l % n

print(k)
