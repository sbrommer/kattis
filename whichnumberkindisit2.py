T = int(input())

for _ in range(T):
    N = int(input())
    o, s = bool(N % 2), int(N ** 0.5) ** 2 == N

    if o:
        print('O', end='')
    if s:
        print('S', end='')
    if not (o or s):
        print('EMPTY', end='')

    print()
