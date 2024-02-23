N = int(input())

for n in range(N):
    if (n + 1) * (n + 2) * (n + 3) >= N:
        print(n)
        break
