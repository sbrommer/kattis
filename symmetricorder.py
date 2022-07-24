n = int(input())
i = 1

while n:
    names = [input() for _ in range(n)]

    asc = names[0::2]
    desc = names[1::2]
    desc.reverse()

    print('SET', i, *asc + desc)

    n = int(input())
    i += 1
