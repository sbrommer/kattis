N = int(input())

TB = 2 * N
LR = 2 * N

for _ in range(N):
    T, B, L, R = list(map(int, input().strip()))

    TB -= T + B
    LR -= L + R

M = min(TB, LR) // 2

print(M, TB - 2 * M, LR - 2 * M)
