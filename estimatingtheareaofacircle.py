from sys import stdin
from math import pi

line = stdin.readline()

while line != '0 0 0\n':
    (r, m, c) = line.split()

    r = float(r)
    m = int(m)
    c = int(c)

    print(pi * r**2, (r * 2)**2 * c / m)

    line = stdin.readline()
