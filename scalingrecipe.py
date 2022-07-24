n, x, y = map(int, input().split())

print(*[y * int(input()) // x for _ in range(n)])
