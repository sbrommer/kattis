from sys import stdin
from math import sqrt, acos, pi, sin

def readfloats():
    return list(map(float, stdin.readline().split()))

fs = readfloats()

while fs:
    r, x, y = fs
    d = sqrt(x ** 2 + y ** 2)

    if d >= r:
        print('miss')

    else:
        theta = 2 * acos(d / r)

        area_segment = r ** 2 / 2 * (theta - sin(theta))
        area_circle = pi * r ** 2

        print(area_circle - area_segment, area_segment)

    fs = readfloats()
