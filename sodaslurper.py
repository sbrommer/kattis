from sys import stdin

e, f, c = list(map(int, stdin.readline().split()))

b = e + f
s = 0

while b // c > 0:
    s += b // c
    b = b // c + b % c

print(s)