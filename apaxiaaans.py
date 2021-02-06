import sys
from itertools import groupby

name = sys.stdin.readline()

print(''.join([c[0] for c in groupby(name)]))
