from sys import stdin

(r, c, zr, zc) = list(map(int, stdin.readline().split()))

for _ in range(r):
    line = stdin.readline()
    for _ in range(zr):
        for i in range(c):
            for _ in range(zc):
                print(line[i], end='')
        print()
