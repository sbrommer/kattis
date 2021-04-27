from sys import stdin

n = int(stdin.readline())
n /= 10000
print(1 if int(n) == 555 else 0)
