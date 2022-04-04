from sys import stdin

n = int(stdin.readline())

cups = []

for _ in range(n):
    a, b = stdin.readline().split()
    if a.isnumeric():
        cups.append((b, int(a) / 2))
    if b.isnumeric():
        cups.append((a, int(b)))

cups.sort(key=lambda cup: cup[1])

for cup in cups:
    print(cup[0])