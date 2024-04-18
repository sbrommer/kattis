def readints():
    return [int(n) for n in input().split()]


def complete(w, h, xs):
    W, H = 0, 0

    for x in xs:
        W += x
        if W > w:
            return False
        if W == w:
            W = 0
            if (H := H+1) == h:
                return True

    return False


h, w, _ = readints()
xs = readints()

print('YES' if complete(w, h, xs) else 'NO')
