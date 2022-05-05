N, M = [int(x) for x in input().split()]

blank = [True] * M

for _ in range(N):
    line = input().strip()
    blank = [b and c == '_' for (b, c) in zip(blank, line)]

print(1 + sum(blank))
