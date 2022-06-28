P = int(input())

for _ in range(P):
    # parse
    K, f = input().split()
    p, q = map(int, f.split('/'))

    # reconstruct path
    path = 0
    height = 0
    while (p, q) != (1, 1):
        if p > q:             # right child
            p -= q
            path |= 1 << height
        else:                 # left child
            q -= p
        height += 1

    # calculate n based on path
    n = 1
    for h in range(height)[::-1]:
        n <<= 1
        n += bool(path & 1 << h)

    print(K, n)
