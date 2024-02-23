from itertools import accumulate, takewhile

n_lph, *locs = open(0).readlines()

lph = int(n_lph.split()[1])
lines = lph * 5

locs = sorted(list(map(int, locs)))

print(len(list(takewhile(lambda x: x <= lines,
                         accumulate(locs)))))
