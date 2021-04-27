from sys import stdin

n = int(stdin.readline())
s = 0

for _ in range(n):
    color = stdin.readline()
    color = color.lower()

    if 'pink' in color or 'rose' in color:
        s += 1

if s == 0:
    print('I must watch Star Wars with my daughter')
else:
    print(s)
