import sys

def f1(xs):
    found = False

    i = 0
    j = len(xs)-1

    while i < j:
        x = xs[i]
        y = xs[j]
        if x != y and x + y == 7777:
            found = True
            break
        if x + y <= 7777:
            i += 1
        else:
            j -= 1

    print('Yes' if found else 'No')


def f2(xs):
    s = set(xs)

    print('Unique' if len(s) == len(xs) else 'Contains duplicate')

def f3(xs):
    n = len(xs)
    i = 0
    x = -1

    while i < n:
        c = 0
        while i+c < n and xs[i+c] == xs[i]:
            c += 1
        if c > n / 2:
            x = xs[i]
            break
        i += c

    print(x)

def f4(xs):
    xs.sort()

    n = len(xs)
    m = n // 2

    if n % 2 == 0:
        print(xs[m-1], end=' ')

    print(xs[m])

def f5(xs):
    xs = list(filter(lambda x : 100 <= x and x <= 999, xs))
    xs.sort()

    for x in xs:
        print(x, end=' ')

fs = [f1, f2, f3, f4, f5]

(n, t) = list(map(int, sys.stdin.readline().split()))

xs = list(map(int, sys.stdin.readline().split()))
xs.sort()

fs[t-1](xs)