from sys import stdin

def readint():
    return int(stdin.readline())

t = readint()

for _ in range(t):
    k = readint()

    p = 0
    for s in range(k):
        p = (p + 0.5) * 2
    print(int(p))
