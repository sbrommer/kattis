from sys import stdin

p, n = list(map(int, stdin.readline().split()))

parts = set()
paradox = False
for i in range(n):
    parts.add(stdin.readline().strip())
    if len(parts) == p:
        paradox = True
        print(i+1)
        break

if not paradox:
    print('paradox avoided')