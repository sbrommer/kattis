v = 0
d = 0
t = 0

for line in open(0).readlines():
    t_str, *v_str = line.split()
    h, m, s = map(int, t_str.split(':'))
    t_new = h + m / 60 + s / 3600
    d += v * (t_new - t)
    t = t_new

    if v_str:
        v = int(v_str[0])
    else:
        print(f'{t_str} {d:.2f} km')
