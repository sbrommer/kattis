import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    xs = list(map(int, sys.stdin.readline().split()))

    print((max(xs) - min(xs)) * 2)