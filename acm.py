from collections import defaultdict

line = input()

entries = defaultdict(int)
rights = set()

while line != '-1':
    m, p, w = line.split()

    if w == 'wrong':
        entries[p] += 20

    else:
        entries[p] += int(m)
        rights.add(p)

    line = input()

points = sum(map(entries.get, rights))

print(len(rights), points)
