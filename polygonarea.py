while n := int(input()):
    vs = [[int(x) for x in input().split()]
          for _ in range(n)]

    area = 0

    for u, v in zip(vs, vs[1:] + [vs[0]]):
        area += (u[0] + v[0]) * (v[1] - u[1])

    cw = area <= 0
    area = abs(area) / 2

    print(f'{"CW" if cw else "CCW"} {area:.1f}')
