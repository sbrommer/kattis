import sys

n = int(sys.stdin.readline())

for _ in range(n):
    x = int(sys.stdin.readline())
    print(x, 'is', 'even' if x % 2 == 0 else 'odd')
