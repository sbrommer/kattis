from sys import stdin

def readmeasurement():
    t, v = stdin.readline().split()
    return int(t), float(v)

n = int(stdin.readline())

ms = []
for _ in range(n):
    ms.append(readmeasurement())

a = 0
for i in range(n-1):
    a += (ms[i][1] + ms[i+1][1]) / 2 * (ms[i+1][0] - ms[i][0])
print(a / 1000)
