def readnumber():
    return int(''.join(input().split()))


def printnumber(n):
    print(*[d for d in str(n)], sep=' ')


t = int(input())

for _ in range(t):
    n1 = readnumber()
    n2 = readnumber()
    printnumber(n1 + n2)
