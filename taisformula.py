def readmeasurement():
    t, v = input().split()
    return int(t), float(v)


N = int(input())

ms = [readmeasurement() for _ in range(N)]

a = 0
for i in range(N - 1):
    a += (ms[i][1] + ms[i+1][1]) / 2 * (ms[i+1][0] - ms[i][0])
print(a / 1000)
