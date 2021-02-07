from sys import stdin

def readint():
    return int(stdin.readline())

def readsegments():
    segments = stdin.readline().split()

    bs = filter(lambda s : s[-1] == 'B', segments)
    rs = filter(lambda s : s[-1] == 'R', segments)

    bs = list(map(lambda b : int(b[:-1]), bs))
    rs = list(map(lambda r : int(r[:-1]), rs))

    bs.sort(reverse=True)
    rs.sort(reverse=True)

    return bs, rs

n = readint()

for i in range(1, n+1):
    print('Case #' + str(i) + ':', end=' ')

    s = readint()
    bs, rs = readsegments()

    l = min(len(bs), len(rs))

    print(sum(bs[:l] + rs[:l]) - 2 * l)

