def readints():
    return [int(n) for n in input().split()]


def lowpressure(forecast):
    for r, line in enumerate(forecast[1:-1]):
        for c, pressure in enumerate(line[1:-1]):
            if all([forecast[r+1+dr][c+1+dc] > pressure
                    for dr, dc in [(0, -1), (0, 1), (-1, 0), (1, 0)]]):
                return 'Jebb'

    return 'Neibb'


n, m = readints()

forecast = [readints() for _ in range(n)]

print(lowpressure(forecast))
