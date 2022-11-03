T = int(input())

for _ in range(T):
    N = list(input().strip())

    for i in range(len(N) - 1, -1, -1):
        if N[i] != '0':
            N[i] = str(int(N[i]) - 1)
            break

    print(int(''.join(N)))
