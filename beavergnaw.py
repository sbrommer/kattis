from math import pi


def readints():
    return map(int, input().split())


D, V = readints()

while (D, V) != (0, 0):
    d = (D ** 3 - 6 * V / pi) ** (1 / 3)
    print(d)
    D, V = readints()
