from sys import stdin

t = int(stdin.readline())

for _ in range(t):
    line = stdin.readline().strip()
    if line.startswith('simon says '):
        print(line.replace('simon says ', ''))
    else:
        print()