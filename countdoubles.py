from more_itertools import windowed


def readints():
    return [int(n) for n in input().split()]


_, m = readints()
A = readints()


print(sum(sum(not i % 2 for i in a) >= 2
          for a in windowed(A, m)))
