g, s, c = map(int, input().split())

bp = 3 * g + 2 * s + c

if bp >= 8:
    print('Province or')
elif bp >= 5:
    print('Duchy or')
elif bp >= 2:
    print('Estate or')

if bp >= 6:
    print('Gold')
elif bp >= 3:
    print('Silver')
else:
    print('Copper')
