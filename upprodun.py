N = int(input())
M = int(input())

k, m = divmod(M, N)

for i in range(N):
    print('*' * (k + (i < m)))
