f, s, g, u, d = map(int, input().split())


def pushes():
    q = [(0, s)]
    visited = {s}

    while q:
        (p, floor), *q = q

        if floor == g:
            return p

        for nxt in [floor - d, floor + u]:
            if 1 <= nxt <= f and nxt not in visited:
                q += [(p+1, nxt)]
                visited |= {nxt}

    return -1


p = pushes()

print(p if p >= 0 else 'use the stairs')
