N = int(input())

probs = sorted([float(input().split()[1]) for _ in range(N)], reverse=True)

print(sum((i + 1) * p for i, p in enumerate(probs)))
