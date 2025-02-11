input()
S = input()

A, H, a, h = 0, 0, 0, 0

for winner in S:
    a += winner == 'A'
    h += winner == 'H'
    if a == 3:
        A += 1
        a, h = 0, 0
    if h == 3:
        H += 1
        a, h = 0, 0

print('Arnar' if H > A else 'Hannes')
