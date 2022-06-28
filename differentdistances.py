line = input()

while line != '0':
    x1, y1, x2, y2, p = map(float, line.split())

    x = abs(x1 - x2) ** p
    y = abs(y1 - y2) ** p

    print((x + y) ** (1 / p))

    line = input()
