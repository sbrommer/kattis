from sys import stdin

line = stdin.readline()

while line != '0\n':
    x1, y1, x2, y2, p = list(map(float, line.split()))

    x = abs(x1 - x2) ** p
    y = abs(y1 - y2) ** p

    print((x + y) ** (1 / p))

    line = stdin.readline()


