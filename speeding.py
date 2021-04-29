from sys import stdin

def readints():
    return list(map(int, stdin.readline().split()))

n = int(stdin.readline())

speed = 0

t1, d1 = readints()
for _ in range(1, n):
    t2, d2 = readints()
    speed = max(speed, (d2 - d1) / (t2 - t1))
    t1, d1 = t2, d2

print(int(speed))
