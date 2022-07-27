N, P, Q = map(int, input().split())

print('opponent' if (P + Q) // N % 2 else 'paul')
