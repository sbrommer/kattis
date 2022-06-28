def int_to_leds(n):
    leds = ''

    for i in range(4):
        n, m = divmod(n, 2)
        leds += '*' if m else '.'

    return leds


leds = [int_to_leds(int(t)) for t in input()]
leds = leds[:2] + ['    '] + leds[2:]

for row in list(zip(*leds))[::-1]:
    print(*row, sep=' ')
