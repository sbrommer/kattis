from sys import stdin

P = int(stdin.readline())

for _ in range(P):
    K, f = stdin.readline().split()
    p, q = list(map(int, f.split('/')))

    path = 0
    line = 0
    while (p, q) != (1, 1):
        if p > q:
            p -= q
            path |= 1 << line
        else:
            q -= p
        line += 1

    n = 1
    for l in range(line-1, -1, -1):
        n <<= 1
        n += bool(path & (1 << l))

    print(K, n)
