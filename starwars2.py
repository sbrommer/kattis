n = int(input()) // 3
xs = sorted(int(x) for x in input().split())

xs = xs[n:-n] + xs[:n] + xs[-n:]
print(*xs)
