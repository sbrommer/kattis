from sys import stdin

def readints():
    return list(map(int, stdin.readline().split()))

w, l = readints()

while [w, l] != [0, 0]:
    robot = [0, 0]
    actually = [0, 0]

    n = int(stdin.readline())

    for _ in range(n):
        d, m = stdin.readline().split()
        m = int(m)

        if d == 'd' or d == 'l':
            m *= -1

        if d == 'l' or d == 'r':
            robot[0]    += m
            actually[0] += m

            actually[0] = max(min(actually[0], w - 1), 0)

        if d == 'd' or d == 'u':
            robot[1]    += m
            actually[1] += m

            actually[1] = max(min(actually[1], l - 1), 0)

    print('Robot thinks', robot[0], robot[1])
    print('Actually at', actually[0], actually[1])
    print()

    w, l = readints()
