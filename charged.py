from math import sqrt, pi, inf

# Constants
chars = [(+1 / pi ** 1, '0'),
         (+1 / pi ** 2, 'O'),
         (+1 / pi ** 3, 'o'),
         (-1 / pi ** 3, '.'),
         (-1 / pi ** 2, 'x'),
         (-1 / pi ** 1, 'X'),
         (-inf,         '%')]


# Helper functions
def parse(x, y, s):
    return (int(x), int(y)), s


def V(point, particles):
    sign = lambda s: int(f'{s}1')
    dist = lambda a, b: sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)

    return sum(sign(s) / dist(point, p) for (p, s) in particles.items())


def getchar(point, particles):
    if point in particles:
        return particles[point]

    else:
        for t, char in chars:
            if V(point, particles) > t:
                return char


# Read input
o = open(0)

n, m, _ = [int(x) for x in o.readline().split()]

particles = dict([parse(*line.split()) for line in o])

# Print charges
for y in range(n):
    for x in range(m):
        print(getchar((x+1, y+1), particles), end='')

    print()
