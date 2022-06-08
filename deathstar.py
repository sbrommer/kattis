o = open(0)

N = int(o.readline())

A = [0] * N

for i in range(N):
    row = [int(n) for n in o.readline().split()]

    for j in range(N):
        if j != i:
            A[j] = max(A[j], row[j])

print(*A)
