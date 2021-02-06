import sys

n = int(sys.stdin.readline())

while n >= 0:
    d = 0
    t_old = 0

    for _ in range(n):
        line = sys.stdin.readline()
        (s, t) = map(int, line.split())
        d += s * (t - t_old)
        t_old = t

    print(d, 'miles')

    n = int(sys.stdin.readline())

