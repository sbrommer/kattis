lines = open(0).readlines()

for line in lines:
    M, d, y, r, s = line.split()

    rh, rm = [int(x) for x in r.split(':')]
    sh, sm = [int(x) for x in s.split(':')]

    rm += rh * 60
    sm += sh * 60

    m = sm - rm
    h, m = divmod(m, 60)

    print(f'{M} {d} {y} {h} hours {m} minutes')
