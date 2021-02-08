from sys import stdin

def readint():
    return int(stdin.readline())

def sod(n):
    return sum(map(int, str(n)))

n = readint()
while n != 0:
    p = 11
    while sod(p*n) != sod(n):
        p += 1

    print(p)

    n = readint()
