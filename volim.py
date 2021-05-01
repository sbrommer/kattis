from sys import stdin

K = int(stdin.readline())
N = int(stdin.readline())

t = 0

for _ in range(N):
    T, Z = stdin.readline().strip().split()

    t += int(T)
    if t >= 3 * 60 + 30:
        break

    K += Z == 'T'

K %= 8

print(8 if K == 0 else K)
