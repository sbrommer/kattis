def readints():
    return list(map(int, input().split()))


room = readints()

while room != [0, 0]:
    robot = [0, 0]
    actual = [0, 0]

    n, = readints()

    for _ in range(n):
        d, m = input().split()

        m = int(m) * (1 - 2 * int(d in 'dl'))
        i = d in 'du'

        robot[i] += m
        actual[i] += m
        actual[i] = max(min(actual[i], room[i] - 1), 0)

    print('Robot thinks', robot[0], robot[1],
          'Actually at', actual[0], actual[1])

    room = readints()
