for n in [int(line) for line in open(0).readlines()]:
    sum_divisors = 1 + sum(sum({d, n // d})
                           for d in range(2, int(n ** 0.5) + 1)
                           if not n % d)

    if n == sum_divisors:
        print(f'{n} perfect')

    elif abs(n - sum_divisors) <= 2:
        print(f'{n} almost perfect')

    else:
        print(f'{n} not perfect')
