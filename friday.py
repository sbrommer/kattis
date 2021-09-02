from sys import stdin

T = int(stdin.readline())

for _ in range(T):
    D, M = list(map(int, stdin.readline().split()))
    ds = list(map(int, stdin.readline().split(' ')))

    days = []
    for d in ds:
        days += range(1, d+1)

    n = 0
    for i in range(5, D, 7):
        if days[i] == 13:
            n += 1

    print(n)
