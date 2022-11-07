from statistics import median

def readints():
    return [int(i) for i in input().split()]

readints()
distances = zip(readints(), readints(), readints())
medians = map(median, distances)

print(*medians)
