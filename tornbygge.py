from sys import stdin

N = int(stdin.readline())
xs = list(map(int, stdin.readline().split()))

t = 1
for i in range(N-1):
    t += xs[i+1] > xs[i]

print(t)
