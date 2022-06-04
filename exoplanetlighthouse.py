from math import acos

o = open(0)


def readreals():
    return [float(r) for r in o.readline().split()]


t = int(o.readline())

for _ in range(t):
    R, h1, h2 = readreals()

    phi = acos(R / (R + h1 / 1000)) +\
          acos(R / (R + h2 / 1000))

    print(R * phi)
