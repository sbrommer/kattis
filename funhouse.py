def readints():
    return map(int, input().split())


def parse_house(L):
    house = []

    for y in range(L):
        line = list(input())
        house.append(line)

        if '*' in line:
            entrance = line.index('*'), y

    return house, entrance


def find_exit(house, W, L, x, y):
    # initialise
    dx = -1 if x == W - 1 else int(x == 0)
    dy = -1 if y == L - 1 else int(y == 0)

    x += dx
    y += dy

    # walk
    while house[y][x] != 'x':
        if house[y][x] in '/\\':
            dx, dy = dy, dx

        if house[y][x] == '/':
            dx, dy = -dx, -dy

        x += dx
        y += dy

    return x, y


n = 1
W, L = readints()

while W + L:
    print('HOUSE', n)

    house, entrance = parse_house(L)

    # find exit and print house
    x, y = find_exit(house, W, L, *entrance)
    house[y][x] = '&'

    for line in house:
        print(*line, sep='')

    n += 1
    W, L = readints()
