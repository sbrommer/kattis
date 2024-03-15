from itertools import groupby

print(''.join(k for k, _ in groupby(input())))
