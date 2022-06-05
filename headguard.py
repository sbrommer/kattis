from itertools import groupby

for line in open(0).readlines():
    print(''.join([str(len(list(g))) + v for v, g in groupby(line.strip())]))
