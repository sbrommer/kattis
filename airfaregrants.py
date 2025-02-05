N = int(input())
Ps = [int(input()) for _ in range(N)]

print(max(0, min(Ps) - max(Ps) // 2))
