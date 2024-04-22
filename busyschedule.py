from re import findall


def key(line):
    h, m, ap = findall(r'(\d*):(\d*) ([ap]).m.', line)[0]
    return (int(h) % 12 + 12 * (ap == 'p'), int(m))


while n := int(input()):
    print(*sorted([input() for _ in range(n)], key=key), sep='\n', end='\n\n')
