from sys import stdin

def readint():
    return int(stdin.readline())

n = readint()

while n != 0:
    names = []
    for _ in range(n):
        names.append(stdin.readline().strip())

    names.sort(key=lambda name: name[0:2])

    for name in names:
        print(name)
    print()

    n = readint()