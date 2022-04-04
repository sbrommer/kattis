from sys import stdin
from math import pi

circle = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ \''

n = int(stdin.readline())

for _ in range(n):
    aphorism = stdin.readline().strip()

    d_letters = 0

    for i in range(len(aphorism) - 1):
        i_letter1 = circle.index(aphorism[i])
        i_letter2 = circle.index(aphorism[i+1])

        d_letter = abs(i_letter2 - i_letter1)
        d_letter = min(d_letter, 28 - d_letter)

        d_letters += d_letter

    d_feet = 2 * pi * 30 * d_letters / 28

    time = d_feet / 15 + len(aphorism)

    print(time)