from math import ceil


def getints():
    return list(map(int, input().split()))


S, N = getints()
As = getints()

gaps = [S - 1] if len(As) == 1 else\
       [(a2 - a1) % S - 1 for a1, a2 in zip(As, As[1:] + [As[0]])]

print(sum(ceil((gap - 2) / 2) for gap in gaps))
