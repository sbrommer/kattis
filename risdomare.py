N = int(input())
s = input() == 'storlek'
portions = [[int(x) for x in input().split()] for _ in range(N)]

mx = max(portions, key=lambda p: (sum(p), p[s]))

print(portions.index(mx) + 1)
