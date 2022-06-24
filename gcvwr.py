def readints():
    return [int(n) for n in input().split()]


G, T, N = readints()
ws = sum(readints())

print(int((G - T) * 0.9 - ws))
