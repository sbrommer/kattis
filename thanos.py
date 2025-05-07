T = int(input())

for _ in range(T):
    P, R, F = map(int, input().split())

    year = 0
    while P * R ** year <= F:
        year += 1

    print(year)
