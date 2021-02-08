from sys import stdin

def readint():
    return int(stdin.readline())

def readlist(n):
    l = []
    for _ in range(n):
        l.append(readint())
    return l

n = readint()

while n != 0:
    l1 = readlist(n)
    l2 = readlist(n)

    l1s = list(l1)
    l1s.sort()
    l2s = list(l2)
    l2s.sort()

    l2.sort(key=lambda i: l1.index(l1s[l2s.index(i)]))

    for i in l2:
        print(i)
    print()

    n = readint()
