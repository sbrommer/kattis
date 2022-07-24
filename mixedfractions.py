def readfraction():
    return map(int, input().split())


n, d = readfraction()
while (n, d) != (0, 0):
    print(n // d, n % d, '/', d)

    n, d = readfraction()
