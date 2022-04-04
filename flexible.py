from sys import stdin

def readints():
    return list(map(int, stdin.readline().split()))

w, p = readints()
ls = readints()
ls = [0] + ls + [w]

widths = set()

for l1 in ls:
    for l2 in ls:
        widths.add(abs(l2 - l1))

widths = list(filter(lambda width: width != 0, widths))
widths.sort()

print(' '.join(map(str, widths)))