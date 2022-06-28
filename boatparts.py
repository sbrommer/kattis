def paradox():
    P, N = map(int, input().split())

    parts = set()

    for i in range(N):
        parts.add(input())
        if len(parts) == P:
            return i + 1

    return 0


p = paradox()

print(p if p else 'paradox avoided')
