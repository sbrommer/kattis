line = open(0).readline().strip()
time = [int(c) for c in line]

def int_to_leds(n):
    leds = ''

    for i in range(4):
        n, m = divmod(n, 2)
        leds += '*' if m else '.'

    return leds

leds = [int_to_leds(n) for n in time]
leds = leds[:2] + ['    '] + leds[2:]

leds_T = [''.join(led) for led in zip(*leds)]
leds_T.reverse()

for row in leds_T:
    print(*row, sep=' ')
