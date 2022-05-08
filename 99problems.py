N = int(input())

d, m = divmod(N, 100)

print(max(99, d * 100 + (-1 if m < 49 else 99)))
