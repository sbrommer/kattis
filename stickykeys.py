from itertools import groupby

print(''.join(i[0] for i in groupby(input())))
