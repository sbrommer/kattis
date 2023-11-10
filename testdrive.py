def signum(n):
    return -1 if n < 0 else 1 if n > 0 else 0


a, b, c = map(int, input().split())

d1 = b - a
d2 = c - b

if d1 == d2:
    print('cruised')

elif signum(d1) != signum(d2):
    print('turned')

elif abs(d2) > abs(d1):
    print('accelerated')

else:
    print('braked')
