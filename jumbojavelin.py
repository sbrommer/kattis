def readint():
    return int(input())


n = readint()
s = sum(readint() for _ in range(n))

print(s - n + 1)
