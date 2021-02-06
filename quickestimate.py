from sys import stdin

n = int(stdin.readline())

for _ in range(n):
    e = stdin.readline()[:-1]
    print(len(e))