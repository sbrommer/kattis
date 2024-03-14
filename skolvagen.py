crossings = input()

N = 0
S = 1

for c in crossings[::-1]:
    if c == 'N':
        N = min(1 + N, 1 + S)
        S = min(2 + N, S)
    if c == 'S':
        N = min(N, 2 + S)
        S = min(1 + N, 1 + S)
    if c == 'B':
        N = min(1 + N, 2 + S)
        S = min(2 + N, 1 + S)

print(N)
