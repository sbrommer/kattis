n, k = map(int, input().split())

r = sum(int(input()) for _ in range(k))

min = (r - (n - k) * 3) / n
max = (r + (n - k) * 3) / n

print(min, max)
