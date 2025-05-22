from itertools import cycle


def makeline(p, *scanline):
    scanline = map(int, scanline)
    ps = {'#': '#.', '.': '.#'}
    return ''.join(p*i
                   for p, i in
                   zip(cycle(ps[p]), scanline))


n = int(input())

while n:
    lines = [makeline(*input().split())
                      for _ in range(n)]

    print(*lines, sep='\n')
    if len(set(map(len, lines))) != 1:
        print('Error decoding image')

    n = int(input())
    if n:
        print()
