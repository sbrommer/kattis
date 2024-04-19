def readfloats():
    return [float(f) for f in input().split()]


d, N = readfloats()

while N := int(N):
    hives = [readfloats() for _ in range(N)]

    sour = sum(any(0 < ((x1-x2)**2 + (y1-y2)**2) ** 0.5 <= d
                   for x1, y1 in hives)
               for x2, y2 in hives)

    print(f'{sour} sour, {len(hives) - sour} sweet')

    d, N = readfloats()
