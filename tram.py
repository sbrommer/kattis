from operator import sub

o = open(0)


def readints():
    return [int(n) for n in o.readline().split()]


N = readints()[0]

print(sum(-sub(*readints()) / N for _ in range(N)))
