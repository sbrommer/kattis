from math import sqrt

t = int(input())

for _ in range(t):
    m = input()
    s = int(sqrt(len(m)))

    for c in range(s):
        for r in range(s):
            print(m[r * s + (s - c - 1)], end='')

    print()
