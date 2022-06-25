from operator import ne


def readstring():
    return [int(c) for c in input().strip()]


s1 = readstring()
s2 = readstring()

print(2 ** sum(map(ne, s1, s2)))
