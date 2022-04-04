from sys import stdin

def readints():
    return list(map(int, stdin.readline().split()))

n = stdin.readline()

while n != '':
    n = int(n)

    ds = {'stack' : [], 'queue' : [], 'priority queue' : []}
    ps = {'stack' : True, 'queue' : True, 'priority queue' : True}

    for _ in range(n):
        t, x = readints()

        if t == 1:
            for d in ds.values():
                d.append(x)

        if t == 2:
            if len(ds['stack']) == 0:
                for p in ps.keys():
                    ps[p] = False

            else:
                if ds['stack'].pop() != x:
                    ps['stack'] = False

                if ds['queue'].pop(0) != x:
                    ps['queue'] = False

                ds['priority queue'].sort()
                if ds['priority queue'].pop() != x:
                    ps['priority queue'] = False

    ps = list(filter(lambda key: ps[key] , ps.keys()))
    
    if len(ps) == 0:
        print('impossible')
    elif len(ps) == 1:
        print(ps[0])
    else:
        print('not sure')

    n = stdin.readline()