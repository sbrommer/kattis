from itertools import islice


def tail(it):
    return islice(it, 1, None)


def readints():
    return map(int, input().split())


n, m = readints()

pieces = set()
for _ in range(n):
    pieces |= {*tail(readints())}

print('Jebb' if len(pieces) == m else 'Neibb')
