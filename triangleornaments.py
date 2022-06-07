from math import sqrt, cos, acos, pi as π

o = open(0)


def gettriangle():
    return [int(n) for n in o.readline().split()]


# calculate median to side C
def median(A, B, C):
    return sqrt((2 * A * A + 2 * B * B - C * C) / 4)


# calculate angle between side A and B
def angle(A, B, C):
    return acos((A * A + B * B - C * C) / (2 * A * B))


def width(A, B, C):
    M = median(A, B, C)
    α = angle(A, M, C / 2)
    w = cos(π / 2 - α) * A

    return 2 * w


N = int(o.readline())

print(sum(width(*gettriangle()) for _ in range(N)))
