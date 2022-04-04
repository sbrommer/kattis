from sys import stdin

def readints():
    return list(map(int, stdin.readline().split()))

n = int(stdin.readline())

for _ in range(n):
    _, *gnomes = readints()

    for i in range(len(gnomes)):
        if gnomes[i] + 1 != gnomes[i+1]:
            print(i+2)
            break