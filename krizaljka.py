from sys import stdin

A, B = stdin.readline().split()

N = len(A)
M = len(B)

for n in range(N):
    if A[n] in B:
        break

m = B.index(A[n])

for r in range(M):
    if r == m:
        print(A)
    else:
        print('.' * n +
              B[r] +
              '.' * (N - n - 1))
