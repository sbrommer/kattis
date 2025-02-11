N = int(input())
K = (N + 2) // 3
t = N // 3 - (N % 3) % 2

print(K)
print(*([2] * (K - t) + [3] * t))
