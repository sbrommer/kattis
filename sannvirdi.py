from bisect import bisect

n = int(input())
contestants = [input().split() for _ in range(n)]
contestants = [(int(g), n) for n, g in contestants]
contestants = sorted(contestants)

q = int(input())
ideas = [int(input()) for _ in range(q)]

for idea in ideas:
    i = bisect(contestants, idea, key=lambda t: t[0])
    print(contestants[i-1][1] if i else ':(')
