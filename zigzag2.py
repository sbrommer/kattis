from sys import stdin

def readint():
    return int(stdin.readline())

def sign(x):
    if x < 0: return -1
    else: return x > 0

def nub(xs):
    result = []
    x_prev = None

    for x in xs:
        if x != x_prev:
            result.append(x)
            x_prev = x

    return result

ds = []
n = readint()

if not n:
    print(0)
else:
    k = readint()
    for _ in range(n-1):
        k2 = readint()
        if k != k2:
            ds.append(sign(k2 - k))
        k = k2

    print(1 + len(nub(ds)))
