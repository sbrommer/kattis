from math import sqrt

T = int(input())

for _ in range(T):
    X, Y = list(map(int, input().split()))

    # Calculate h that gives the biggest volume.
    A = 12
    B = -4 * (X + Y)
    C = X * Y
    D = B ** 2 - 4 * A * C

    h = (-B - sqrt(D)) / (2 * A)

    # Calculate volume.
    a = X - 2 * h
    b = Y - 2 * h
    V = a * b * h

    print(V)
