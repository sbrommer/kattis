def readints():
    return [int(n) for n in input().split()]


n, m = readints()
ts = sorted(readints(), reverse=True)
ls = sorted(readints(), reverse=True)


i = 0

for t in ts:
    if i < len(ls) and t <= ls[i]:
        i += 1

print(i)
