from itertools import accumulate

n = int(input())
stops = [map(int, input().split()) for _ in range(n)]

print(max(accumulate(b-a for a, b in stops)))
