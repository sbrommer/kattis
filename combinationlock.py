def readints():
    return [int(n) for n in input().split()]


def turn(x, y):
    return int((x - y) % 40) * 9


a, b, c, d = readints()

while a + b + c + d:
    print(1080 + turn(a, b) + turn(c, b) + turn(c, d))

    a, b, c, d = readints()
