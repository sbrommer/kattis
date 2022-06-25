def sod(i):
    return sum(map(int, str(i)))


L, D, X = map(int, open(0).readlines())

for N in range(L, D+1):
    if sod(N) == X:
        print(N)
        break

for M in range(D, L-1, -1):
    if sod(M) == X:
        print(M)
        break
