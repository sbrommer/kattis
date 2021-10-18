from sys import stdin
from itertools import combinations

def is_set(a, b, c):
    for i in range(4):
        s = set([a[i], b[i], c[i]])
        if len(s) != 1 and len(s) != 3:
            return False
    return True

cs = []
for _ in range(4):
    cs.extend(stdin.readline().split())

found = False
for (i, j, k) in combinations(range(12), 3):
    if is_set(cs[i], cs[j], cs[k]):
        found = True
        print(i+1, j+1, k+1)

if not found:
    print('no sets')
