from sys import stdin

def readints():
    return list(map(int, stdin.readline().split()))

n, p, s = readints()

for _ in range(s):
    choice = set(readints()[1:])
    print('KEEP' if p in choice else 'REMOVE')
