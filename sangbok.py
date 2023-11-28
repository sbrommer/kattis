def readints():
    return list(map(int, input().split()))


t = readints()[0] * 60

ss = sorted(readints())

m = 0

for s in ss:
    t -= s
    if t >= 0:
        m += s
    if t <= 0:
        break

print(m)
