N = int(input())

first = 2**31

for _ in range(N):
    M, O = map(int, input().split())
    if not O:
        first = min(first, M)

print(-1 if first == 2**31 else first)
