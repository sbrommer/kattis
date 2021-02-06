import sys

n = int(sys.stdin.readline())

for _ in range(n):
    line = sys.stdin.readline()
    if line[:10] == 'Simon says':
        print(line[10:-1])
