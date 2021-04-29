from sys import stdin

N, P, Q = list(map(int, stdin.readline().split()))

print('opponent' if (P + Q) // N % 2 else 'paul')
