from sys import stdin

N = int(stdin.readline())
lines = stdin.readlines()

for i in range(0, N, 2):
    print(lines[i].strip())
