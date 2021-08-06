from sys import stdin
from math import sqrt, acos, pi

def readfloats():
    return list(map(float, stdin.readline().split()))

fs = readfloats()
while fs:
    r, x, y = fs
    d = sqrt(x ** 2 + y ** 2)

    if d >= r:
        print('miss')

    else:
        alpha = acos(d / r)
        area_triangle = d * sqrt(r ** 2 - d ** 2)

        area_sector = alpha * r ** 2
        area_segment = area_sector - area_triangle

        area_circle = pi * r ** 2

        print(area_circle - area_segment, area_segment)

    fs = readfloats()
