R, C = [int(n) for n in input().split()]

cuts = R * C - 1

print('Alf' if cuts % 2 else 'Beata')
