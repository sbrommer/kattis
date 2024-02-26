def readints():
    return [int(n) for n in input().split()]


n, s = readints()

for _ in range(n):
    l, r = readints()
    if l <= s <= r:
        s += 1

print(s)
