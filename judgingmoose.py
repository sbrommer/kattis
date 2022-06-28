l, r = map(int, input().split())

if l + r:
    print('Even' if l == r else 'Odd', 2 * max(l, r))
else:
    print('Not a moose')
