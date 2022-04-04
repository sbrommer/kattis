from sys import stdin

def group(busses):
    gs = []
    while busses: 
        bus, *busses = busses
        g = [bus]
        while busses and bus + 1 == busses[0]:
            bus, *busses = busses
            g.append(bus)
        gs.append(g)
    return gs


n = int(stdin.readline())

busses = list(map(int, stdin.readline().split()))
busses.sort()

groups = group(busses)

for g in groups:
    if len(g) == 1:
        print(g[0], end=' ')
    elif len(g) == 2:
        print(g[0], g[1], end=' ')
    else:
        print(str(g[0]) + '-' + str(g[-1]), end=' ')
