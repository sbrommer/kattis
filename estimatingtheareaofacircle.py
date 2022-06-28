from math import pi


def readfloats():
    return map(float, input().split())


r, m, c = readfloats()

while r + m + c:
    print(pi * r ** 2, (r * 2) ** 2 * c / m)

    r, m, c = readfloats()
