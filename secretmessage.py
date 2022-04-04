from sys import stdin
from math import ceil, sqrt

n = int(stdin.readline())

for _ in range(n):
    original = stdin.readline().strip()

    l = len(original)
    m = ceil(sqrt(l))**2
    k = int(sqrt(m))

    original += '*' * (m-l)

    secret = ''
 
    for c in range(k):
        for r in range(k):
            secret += original[(k-r-1)*k+c]

    secret = ''.join(list(filter(lambda c: c != '*', secret)))

    print(secret)