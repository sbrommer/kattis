from math import sin, cos, radians, hypot


def walk():
    x, y, *instr = input().split()

    p = complex(float(x), float(y))
    d = 1+0j

    for i, x in zip(instr[::2], instr[1::2]):
        x = float(x)

        match i:
            case 'walk':
                p += d * x

            case _:
                d *= complex(cos(radians(x)), sin(radians(x)))

    return p


def dist(a, b):
    d = a - b
    return hypot(d.real, d.imag)


while n := int(input()):
    destinations = [walk() for _ in range(n)]
    μ = sum(destinations) / len(destinations)
    worst = max(dist(μ, d) for d in destinations)

    print(μ.real, μ.imag, worst)
