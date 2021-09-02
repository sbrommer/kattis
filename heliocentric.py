from sys import stdin

def readints():
    return list(map(int, stdin.readline().split()))

input = readints()
c = 1

while len(input) > 0:
    e, m = input
    d = 0

    while e % 365 != m % 687:
        e += 1
        m += 1
        d += 1

    print('Case', c, end='')
    print(':', d)

    c += 1
    input = readints()
