P = int(input())

for _ in range(P):
    K, N = map(int, input().split())
    b = bin(N)[2:]

    p = 0
    q = 1
    for i in range(len(b)):
        if int(b[i]):
            p += q
        else:
            q += p
    print(K, str(p) + '/' + str(q))
