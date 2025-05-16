D = int(input())


def search():
    n1, n2 = 0, 1
    while n1 < n2:
        d = n2 ** 2 - n1 ** 2

        if d < D:
            n2 += 1
        elif D < d:
            n1 += 1
        else:
            return f'{n1} {n2}'

    return 'impossible'


print(search())
