from operator import mul

d = dict(zip('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ',
             [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 8,
              11, 12, 13, 14, 11, 15, 1, 16, 17, 18,
              19, 20, 0, 21, 0, 22, 5, 23, 24, 24,
              25, 26, 24, 2]))

def parse(n):
    return [*map(d.get, n)]


def check(n):
    return sum(map(mul, n, [2, 4, 5, 7, 8, 10, 11, 13])) % 27


def todec(n):
    dec = 0
    for d in n:
        dec *= 27
        dec += d
    return dec


P = int(input())

for _ in range(P):
    K, n = input().split()

    *n, c = parse(n)

    if c == check(n):
        print(K, todec(n))
    else:
        print(K, 'Invalid')
