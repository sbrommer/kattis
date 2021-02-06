from sys import stdin

w = int(stdin.readline())
n = int(stdin.readline())

a = 0

for _ in range(n):
    (wi, li) = list(map(int, stdin.readline().split()))
    a += wi * li

print(a // w)
