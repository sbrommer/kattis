import sys

def sod(i):
    return sum(map(int, str(i)))

l = int(sys.stdin.readline())
d = int(sys.stdin.readline())
x = int(sys.stdin.readline())

for n in range(l, d+1):
    if sod(n) == x:
        print(n)
        break

for m in range(d, l-1, -1):
    if sod(m) == x:
        print(m)
        break