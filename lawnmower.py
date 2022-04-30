o = open(0)


def readfloats():
    return [float(n) for n in o.readline().split()]


def goodjob(xs, w, f):
    xs.sort()

    if 0 < xs[0] - 0.5 * w:
        return False

    if xs[-1] + 0.5 * w < f:
        return False

    return all(x2 - x1 <= w for x1, x2 in zip(xs, xs[1:]))


nx, ny, w = readfloats()

while nx + ny + w:
    xs = readfloats()
    ys = readfloats()

    print('YES' if goodjob(xs, w, 75) and goodjob(ys, w, 100) else 'NO')

    nx, ny, w = readfloats()
