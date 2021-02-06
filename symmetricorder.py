from sys import stdin

n = int(stdin.readline())
i = 1

while n != 0:
    print('SET', i)

    names = []
    for _ in range(n):
        names.append(stdin.readline()[:-1])

    asc = names[0::2]
    desc = names[1::2]
    desc.reverse()

    for name in asc:
        print(name)
    for name in desc:
        print(name)

    n = int(stdin.readline())
    i += 1
