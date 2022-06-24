from itertools import groupby

print(*[c[0] for c in groupby(input())], sep='')
