from sys import stdin

def readfraction():
    return list(map(int, stdin.readline().split()))

n, d = readfraction()
while (n, d) != (0, 0):
    print(n // d, n % d, '/', d)

    n, d = readfraction()
