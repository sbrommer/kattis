o = open(0)

N = int(o.readline())

A = ['0'] * N

for _ in range(N):
    A = [max(*t) for t in zip(A, o.readline().split())]

print(*A)
