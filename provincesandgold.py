from sys import stdin

(g, s, c) = list(map(int, stdin.readline().split()))

bp = 3*g + 2*s + c

if bp >= 8:
    print('Province or', end=' ')
elif bp >= 5:
    print('Duchy or', end=' ')
elif bp >= 2:
    print('Estate or', end=' ')

if bp >= 6:
    print('Gold')
elif bp >= 3:
    print('Silver')
else:
    print('Copper')
