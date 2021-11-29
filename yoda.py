from sys import stdin

def yoda(n, m):
    mask = [cn >= cm for (cn, cm) in zip(n, m)]

    if not sum(mask):
        return 'YODA'

    return int(''.join([c if m else '' for (c, m) in zip(n, mask)]))

n = stdin.readline().strip()
m = stdin.readline().strip()

n = n.rjust(len(m), '0')
m = m.rjust(len(n), '0')

print(yoda(n, m))
print(yoda(m, n))
