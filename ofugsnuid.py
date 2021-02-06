import sys

n = int(sys.stdin.readline())

l = list()

for _ in range(n):
    l.append(int(sys.stdin.readline()))

for i in reversed(range(n)):
    print(l[i])