import sys

n = int(sys.stdin.readline())

for _ in range(n):
    line = sys.stdin.readline()
    (r, e, c) = map(int, line.split())
    if r < e - c:
        print('advertise')
    if r > e - c:
        print('do not advertise')
    if r == e - c:
        print('does not matter')