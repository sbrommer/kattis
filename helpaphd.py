from sys import stdin

n = int(stdin.readline())

for _ in range(n):
    line = stdin.readline().strip()
    if line == 'P=NP':
        print('skipped')
    else:
        a, b = list(map(int, line.split('+')))
        print(a + b)