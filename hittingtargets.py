from sys import stdin
from math import sqrt

targets = {'rectangle' : [],
           'circle'    : []}

m = int(stdin.readline())

for _ in range(m):
    form, *ints = stdin.readline().split()
    targets[form].append(list(map(int, ints)))

n = int(stdin.readline())

for _ in range(n):
    x, y = list(map(int, stdin.readline().split()))

    h = 0

    for [x1, y1, x2, y2] in targets['rectangle']:
        h += x1<=x and x<=x2 and y1<=y and y<=y2

    for [x1, y1, r] in targets['circle']:
        h += sqrt((x1-x)**2 + (y1-y)**2) <= r

    print(h)
