N = int(input())
L, W = map(int, input().split())
ps = sorted(int(input()) for _ in range(N))

N //= 2
delta = L / (N - 1)

mem = [[0] * (N + 1) for _ in range(N + 1)]

for l in range(N+1)[::-1]:
    for r in range(N+1)[::-1]:
        i = l+r
        if l == N and r == N:
            mem[l][r] = 0
        elif l == N:
            mem[l][r] = mem[l][r+1] + ((ps[i] - r*delta)**2 + W**2)**0.5
        elif r == N:
            mem[l][r] = mem[l+1][r] + abs(ps[i] - l*delta)
        else:
            mem[l][r] = min(mem[l][r+1] + ((ps[i] - r*delta)**2 + W**2)**0.5,
                            mem[l+1][r] + abs(ps[i] - l*delta))

print(mem[0][0])
