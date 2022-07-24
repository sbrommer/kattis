def sod(N):
    return sum(map(int, str(N)))


N = int(input())
while N:
    p = 11

    while sod(p * N) != sod(N):
        p += 1

    print(p)

    N = int(input())
