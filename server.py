from sys import stdin

def readints():
    return list(map(int, stdin.readline().split()))

n, T = readints()
ts = readints()

i = 0

while i < n and T-ts[i] >= 0:
    T -= ts[i]
    i += 1

print(i)