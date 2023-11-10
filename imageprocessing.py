def readints():
    return list(map(int, input().split()))


H, W, N, M = readints()

image = [readints() for _ in range(H)]
kernel = [readints()[::-1] for _ in range(N)][::-1]


for h in range(H - N + 1):
    for w in range(W - M + 1):
        c = 0
        for n in range(N):
            for m in range(M):
                c += image[h + n][w + m] * kernel[n][m]
        print(c, end=' ')
    print()
