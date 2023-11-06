h, k, v, s = map(int, input().split())
d = 0

while h:
    v += s
    v -= max(1, v // 10)

    if v >= k:
        h += 1
    elif v > 0:
        h -= 1

    if not h:
        v = 0

    if v < 0:
        h, v = 0, 0

    d += v

    if s > 0:
        s -= 1

print(d)
