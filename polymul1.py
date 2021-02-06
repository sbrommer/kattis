import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n1 = int(sys.stdin.readline())
    cs1 = list(map(int, sys.stdin.readline().split()))
    n2 = int(sys.stdin.readline())
    cs2 = list(map(int, sys.stdin.readline().split()))

    n = n1 + n2

    print(n)

    cs = [0] * (n + 1)

    for i1 in range(n1 + 1):
        for i2 in range(n2 + 1):
            i = i1 + i2
            c = cs1[i1] * cs2[i2]
            cs[i] += c

    for c in cs:
        print(c, end=' ')

    print()