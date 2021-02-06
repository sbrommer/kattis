import sys

line = sys.stdin.readline()
pieces = list(map(int, line.split()))
should = [1, 1, 2, 2, 2, 8]

for i in range(6):
    print(should[i] - pieces[i], end=' ')
