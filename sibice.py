import sys

line = sys.stdin.readline()
(n, w, h) = map(int, line.split())

for _ in range(n):
    m = int(sys.stdin.readline())

    print('DA' if m**2 <= w**2  +h**2 else 'NE')
