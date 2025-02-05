def readints():
    return map(int, input().split())


xh, yh = readints()
xp, yp = readints()

print((xh != xp) + (yh != yp))
