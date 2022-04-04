from sys import stdin

def readints():
    return list(map(int, stdin.readline().split()))

n = int(stdin.readline())

f = set()

for _ in range(n):
    s, t = readints()
    f.update(range(s, t+1))

print(len(f))