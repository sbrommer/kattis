from sys import stdin

(l, r) = list(map(int, stdin.readline().split()))

if l + r == 0:
    print('Not a moose')
else:
    if l == r:
        print('Even', end=' ')
    else:
        print('Odd', end=' ')
    print(2 * max(l, r))
