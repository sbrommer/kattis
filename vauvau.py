from sys import stdin

(a, b, c, d) = list(map(int, stdin.readline().split()))

men = list(map(int, stdin.readline().split()))

output = ['none', 'one', 'both']

for m in men:
    m -= 1

    d1 = m % (a + b)
    d2 = m % (c + d)

    n = (d1 < a) + (d2 < c)

    print(output[n])
