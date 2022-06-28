from math import pi

circle = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ \''

N = int(input())

for _ in range(N):
    aphorism = input()

    ds = 0

    for i in range(len(aphorism) - 1):
        i1 = circle.index(aphorism[i])
        i2 = circle.index(aphorism[i+1])

        d = abs(i2 - i1)
        d = min(d, 28 - d)

        ds += d

    d_feet = 2 * pi * 30 * ds / 28

    time = d_feet / 15 + len(aphorism)

    print(time)
