from sys import stdin

def readints():
    return list(map(int, stdin.readline().split()))

x, y = readints()
while (x, y) != (0, 0):
    if x + y == 13:
        print('Never speak again.')
    else:
        if x > y:
            print('To the convention.')
        if x < y:
            print('Left beehind.')
        if x == y:
            print('Undecided.')

    x, y = readints()