from operator import mul


def getfloats():
    return [float(i) for i in input().split()]


n = int(input())
qaly = sum(mul(*getfloats()) for _ in range(n))

print(qaly)
