from itertools import accumulate


def readints():
    return [int(n) for n in input().split()]


input()
As = sorted(readints())
As = list(accumulate(As))
Bs = readints()

for B in Bs:
    print(As[B-1])
