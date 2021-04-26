from sys import stdin

def readint():
    return int(stdin.readline())

n = readint()
s = 0

for _ in range(n):
    s += readint()

print(s - n + 1)
