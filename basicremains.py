while (line := input()) != '0':
    b, p, m = line.split()
    b = int(b)
    p = int(p, b)
    m = int(m, b)

    n = p % m

    if n == 0:
        print(0)
    else:
        s = ''

        while n:
            s = f'{n % b}' + s
            n //= b

        print(s)
