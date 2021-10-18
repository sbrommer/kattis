from sys import stdin

def parseints(line):
    return map(int, line.split())

line = stdin.readline().strip()

while line != '0':
    k, m = list(parseints(line))
    chosen = set(parseints(stdin.readline()))

    reqs = True
    for _ in range(m):
        c, r, *courses = list(parseints(stdin.readline()))

        if len(chosen.intersection(set(courses))) < r:
            reqs = False

    print('yes' if reqs else 'no')

    line = stdin.readline().strip()
