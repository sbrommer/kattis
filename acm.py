import sys

line = sys.stdin.readline()[:-1]

entries = {}
rights = set()

while line != '-1':
    (m, p, w) = line.split()
    m = int(m)

    if p not in entries.keys():
        entries[p] = 0

    if w == 'wrong':
        entries[p] += 20

    else:
        entries[p] += m
        rights.add(p)

    line = sys.stdin.readline()[:-1]

points = 0

for right in rights:
    points += entries[right]

print(len(rights), points)