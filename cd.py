import sys

line = sys.stdin.readline()

while line != '0 0\n':
    (n, m) = map(int, line.split())

    jack = set()
    for _ in range(n):
        jack.add(int(sys.stdin.readline()))

    jill = set()
    for _ in range(m):
        jill.add(int(sys.stdin.readline()))

    print(len(jack & jill))

    line = sys.stdin.readline()
