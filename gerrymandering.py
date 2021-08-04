from sys import stdin
from math import floor

def readints():
    return list(map(int, stdin.readline().split()))

P, D = readints()

votes = [[0, 0] for _ in range(D)]
V = 0

for _ in range(P):
    d, a, b = readints()

    votes[d-1][0] += a
    votes[d-1][1] += b
    V += a + b

w_a = 0
w_b = 0

for d in range(D):
    a, b = votes[d]
    majority = floor((a + b) / 2) + 1

    if a > b:
        winner = 'A'
        a -= majority
    else:
        winner = 'B'
        b -= majority

    w_a += a
    w_b += b

    print(winner, a, b)

print(abs(w_a - w_b) / V)

