o = open(0)

volume = 7

n = int(o.readline())

for _ in range(n):
    if o.readline().strip() == 'Skru op!':
        volume = min(volume + 1, 10)

    else:
        volume = max(volume - 1, 0)

print(volume)
