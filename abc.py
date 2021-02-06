from sys import stdin

ints = list(map(int, stdin.readline().split()))
order = stdin.readline()[:-1]

ints.sort()
order = list(map(lambda o : ord(o) - ord('A'), order))

for o in order:
    print(ints[o], end=' ')
