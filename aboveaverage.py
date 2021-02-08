from sys import stdin
from statistics import mean

c = int(stdin.readline())

for _ in range(c):
    c, *ns = list(map(int, stdin.readline().split()))

    above_avg = list(filter(lambda n: n > mean(ns), ns))

    p = 100 * len(above_avg) / c

    print('%.3f'%p + '%')
