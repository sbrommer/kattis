def readints():
    return map(int, input().split())


N, = readints()

f = set()

for _ in range(N):
    s, t = readints()
    f.update(range(s, t+1))

print(len(f))
