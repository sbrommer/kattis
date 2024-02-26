from statistics import mean

t = int(input())

for _ in range(t):
    n = int(input().split()[0])
    bs = [[int(b) for b in input()] for _ in range(n)]

    print(''.join([str(round(mean(b))) for b in zip(*bs)]))
