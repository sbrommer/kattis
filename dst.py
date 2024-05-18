N = int(input())

for _ in range(N):
    F, D, H, M = input().split()
    DM = ((F == 'F') * 2 - 1) * int(D)
    H, M = int(H), int(M)

    M += DM
    DH, M = divmod(M, 60)
    H += DH
    H %= 24

    print(H, M)
