o = open(0)

def readints():
    return list(map(int, o.readline().split()))

G, T, N = readints()
ω = sum(readints())

max_weight = (G - T) * 0.9


print(int((G - T) * 0.9 - ω))
