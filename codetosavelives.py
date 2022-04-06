o = open(0)


def readnumber():
    return int(''.join(o.readline().split()))


def printnumber(n):
    print(*[d for d in str(n)], sep=' ')


t = int(o.readline())

for _ in range(t):
    n1 = readnumber()
    n2 = readnumber()
    printnumber(n1 + n2)
