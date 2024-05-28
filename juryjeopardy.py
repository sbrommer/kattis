def printgrid(path):
    rows = [p.real for p in path]
    cols = [p.imag for p in path]

    rmin, rmax = int(min(rows)), int(max(rows))
    cmin, cmax = int(min(cols)), int(max(cols))

    print(rmax - rmin + 3, cmax - cmin + 2)

    for r in range(rmin - 1, rmax + 2):
        print(*['.' if complex(r, c) in path else '#'
                for c in range(cmin, cmax + 2)], sep='')


t = int(input())
print(t)

for _ in range(t):
    robot = input()

    p = 0+0j
    d = 0+1j
    path = {p}

    for move in robot:
        match move:
            case 'R':
                d *= 0-1j
            case 'L':
                d /= 0-1j
            case 'B':
                d = -d
        p += d
        path |= {p}

    printgrid(path)
