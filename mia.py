from sys import stdin

def score(d1, d2):
    d1, d2 = min(d1, d2), max(d1, d2)

    if [d1, d2] == [1, 2]:
        return 1000

    if d1 == d2:
        return 100 * d1

    return d2 * 10 + d1

def readints():
    return list(map(int, stdin.readline().split()))

ints = readints()

while sum(ints) > 0:
    s0, s1, r0, r1 = ints

    s = score(s0, s1)
    r = score(r0, r1)

    if s > r:
        print('Player 1 wins.')
    elif r > s:
        print('Player 2 wins.')
    else:
        print('Tie.')

    ints = readints()
