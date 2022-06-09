from math import cos, sin, radians, sqrt

o = open(0)

N = int(o.readline())

for _ in range(N):
    T = int(o.readline())

    x, y = 0, 0
    θ = 0

    for _ in range(T):
        c, n = o.readline().split()
        n = int(n)

        if c == 'lt':
            θ = θ - n

        elif c == 'rt':
            θ = θ + n

        elif c == 'fd':
            x += cos(radians(θ)) * n
            y += sin(radians(θ)) * n

        else:  # c == 'bk'
            x -= cos(radians(θ)) * n
            y -= sin(radians(θ)) * n

    print(round(sqrt(x ** 2 + y ** 2)))
