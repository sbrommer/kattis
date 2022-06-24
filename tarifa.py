def readint():
    return int(input())


X = readint()
N = readint()

print(X * (N + 1) - sum(readint() for _ in range(N)))
