def readlist(n):
    return [int(input()) for _ in range(n)]


n = int(input())

while n:
    l1 = readlist(n)
    l2 = readlist(n)

    l1s = sorted(l1)
    l2s = sorted(l2)

    print(*sorted(l2, key=lambda x: l1.index(l1s[l2s.index(x)])))

    n = int(input())
