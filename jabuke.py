from sys import stdin

def parsecoords():
    return list(map(int, stdin.readline().split()))

def triarea(a, b, c):
    return abs(a[0] * (b[1] - c[1]) +
               b[0] * (c[1] - a[1]) +
               c[0] * (a[1] - b[1])) / 2

a = parsecoords()
b = parsecoords()
c = parsecoords()

N = int(stdin.readline())
A = triarea(a, b, c)

print(A)

t = 0
for _ in range(N):
    p = parsecoords()
    t += triarea(a, b, p) + triarea(b, c, p) + triarea(c, a, p) == A

print(t)
