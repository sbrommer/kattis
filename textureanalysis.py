o = open(0)

line = o.readline().strip()
n = 1

while line != 'END':
    whites = line.split('*')[1:-1]
    counts = map(len, whites)
    even = len(set(counts)) <= 1

    print(n, 'EVEN' if even else 'NOT EVEN')

    line = o.readline().strip()
    n += 1
