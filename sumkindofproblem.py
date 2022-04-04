from sys import stdin

def readint():
    return int(stdin.readline())

def readints():
    return list(map(int, stdin.readline().split()))

p = readint()

for _ in range(p):
    k, n = readints()
    print(k, end=' ')
    print(sum(range(1,n+1)), end=' ')
    print(sum(range(1,2*n,2)), end=' ')
    print(sum(range(2,2*(n+1),2)))
