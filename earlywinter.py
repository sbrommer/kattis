from sys import stdin
from itertools import ifilter

def readints():
    return list(map(int, stdin.readline().split()))

n, dm = readints()
ds = readints()

try:
    k = ifilter(lambda d : d <= dm, ds)
    print(f"It hadn't snowed this early in {k} years!")
except ValueError:
    print('It had never snowed this early!')
