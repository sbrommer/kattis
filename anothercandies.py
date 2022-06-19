o = open(0)


def readint():
    return int(o.readline())


T = readint()

for _ in range(T):
    o.readline()

    N = readint()
    m = sum(readint() for _ in range(N)) % N

    print('NO' if m else 'YES')
