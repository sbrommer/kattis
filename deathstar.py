N = int(input())

A = ['0'] * N

for _ in range(N):
    A = [max(*t) for t in zip(A, input().split())]

print(*A)
