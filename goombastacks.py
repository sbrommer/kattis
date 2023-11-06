N = int(input())

G = 0

for i in range(N):
    g, b = map(int, input().split())

    G += g

    if G < b:
        print('impossible')
        break

    if i == N - 1:
        print('possible')
