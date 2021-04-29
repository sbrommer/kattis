from sys import stdin

n = stdin.readline().count('S')
m = stdin.readline().count('S')

for _ in range(n * m):
    print('S(', end='')

print(0, end='')

for _ in range(n * m):
    print(')', end='')
