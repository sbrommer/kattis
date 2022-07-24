def readints():
    return [int(c) for c in input().split()]


n, k = readints()
xs = list(readints())

print(*xs[k - 1::k])
