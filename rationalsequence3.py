from sys import stdin

P = int(stdin.readline())

for _ in range(P):
    K, N = list(map(int, stdin.readline().split()))
    b = bin(N)[2:]

    p = 0
    q = 1
    for i in range(len(b)):
        if int(b[i]):
            p += q
        else:
            q += p
    print(K, str(p) + '/' + str(q))
