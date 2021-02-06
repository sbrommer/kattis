from sys import stdin

n = int(stdin.readline())

s = 0
a1 = ''

for _ in range(n):
    a2 = stdin.readline()[0]
    s += a1 == a2
    a1 = a2

print(s)
