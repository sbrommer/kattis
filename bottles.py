from math import pi as π


def readfloats():
    return [float(f) for f in input().split()]


def mul(c, P):
    return [a * c for a in P]


def square(P):
    squared = [0] * (len(P) * 2)
    for i, a in enumerate(P):
        for j, b in enumerate(P):
            squared[i + j] += a * b

    return squared


def area(P):
    return mul(π, square(P))


def integrate(P):
    return [0] + [a / (i + 1) for i, a in enumerate(P)]


def apply(P, x):
    return sum(a * x ** i for i, a in enumerate(P))


def volume(P, d, u):
    def F(x): return apply(integrate(area(P)), x)
    return F(u) - F(d)


def binsearch(f, goal, xl, xr, tolerance=0.01):
    x = (xr + xl) / 2
    v = f(x)
    while abs((v := f(x)) - goal) > tolerance:
        if v > goal:
            xr = x
        else:
            xl = x
        x = (xr + xl) / 2
        v = f(x)
    return x


i = 0
while True:
    i += 1
    try:
        n = int(input())
        P = readfloats()
        xlow, xhigh, inc = readfloats()

    except EOFError:
        break

    V = volume(P, xlow, xhigh)

    print(f'Case {i}: {V:.2f}')

    vs = [inc * i for i in range(1, 9) if inc * i <= V]
    def f(h): return volume(P, xlow, h)
    marks = [binsearch(f, v, xlow, xhigh) - xlow for v in vs]

    if marks:
        print(*[f'{m:.2f}' for m in marks])
    else:
        print('insufficient volume')
