from sys import stdin

def readints():
    return list(map(int, stdin.readline().split()))

room = readints()

while room != [0, 0]:
    rob = [0, 0]
    act = [0, 0]

    n = int(stdin.readline())

    for _ in range(n):
        d, m = stdin.readline().split()

        m = int(m) * (1 - 2 * int(d in 'dl'))
        i = d in 'du'

        rob[i] += m
        act[i] += m
        act[i] = max(min(act[i], room[i] - 1), 0)

    print('Robot thinks', rob[0], rob[1])
    print('Actually at', act[0], act[1])
    print()

    room = readints()
