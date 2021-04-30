from sys import stdin

N = int(stdin.readline())

TB = 2 * N
LR = 2 * N

for _ in range(N):
    T, B, L, R = list(map(int, stdin.readline().strip()))

    TB -= T + B
    LR -= L + R

M = min(TB, LR) // 2

print(M, TB - 2 * M, LR - 2 * M)
