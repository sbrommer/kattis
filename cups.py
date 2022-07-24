def readcup():
    a, b = input().split()

    if a.isnumeric():
        return int(a) / 2, b

    return int(b), a


n = int(input())

cups = sorted([readcup() for _ in range(n)])
print(*(cup[1] for cup in cups))
