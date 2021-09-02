from sys import stdin

n = int(stdin.readline())

while n != 0:
    n -= 1
    t = 0
    ts = []

    while n > 0:
        if n % 2:
            ts.append(3**t)
        n //= 2
        t += 1

    print('{', end=' ')
    print(*ts, sep=', ', end=' ')
    print('}')

    n = int(stdin.readline())
