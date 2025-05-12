M = 10**4

for line in open(0).readlines():
    n, op, m = line.split()
    n = int(n)
    m = int(m)

    match op:
        case '+':
            print((n % M + m % M) % M)

        case '*':
            print((n % M * m % M) % M)

        case '^':
            print(pow(n % M, m, M))
