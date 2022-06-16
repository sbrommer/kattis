def transpose(block):
    return list(''.join(col) for col in zip(*block))


def sortcolumns(block):
    block = transpose(block)
    block.sort(key=lambda col: col.lower())
    return transpose(block)


o = open(0)

r, c = [int(n) for n in o.readline().split()]


while (r, c) != (0, 0):
    block = [o.readline().strip() for _ in range(r)]
    block = sortcolumns(block)

    print(*block, sep='\n')
    print()

    r, c = [int(n) for n in o.readline().split()]
