A, B = input().split()

N = len(A)
M = len(B)

for n in range(N):
    if A[n] in B:
        break

m = B.index(A[n])

for r in range(M):
    print(A if r == m else '.' * n + B[r] + '.' * (N - n - 1))
