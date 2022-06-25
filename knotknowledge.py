def readints():
    return set(map(int, input().split()))


readints()

xs = readints()
ys = readints()

print(list(xs - ys)[0])
