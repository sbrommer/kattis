def readints():
    return map(int, input().split())


n, T = readints()
ts = list(readints())

i = 0

while i < n and T - ts[i] >= 0:
    T -= ts[i]
    i += 1

print(i)
