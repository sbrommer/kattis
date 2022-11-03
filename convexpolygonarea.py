n = int(input())

for _ in range(n):
    m, *cs = list(map(int, input().split()))
    x = cs[0::2]
    y = cs[1::2]

    area = 0
    for i in range(m):
        area += x[i] * y[(i + 1) % m]
        area -= y[i] * x[(i + 1) % m]

    print(0.5 * area)
