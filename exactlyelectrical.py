a, b, c, d, t = [int(n) for n in open(0).read().split()]

t -= abs(c - a) + abs(d - b)

print('N' if t < 0 or t % 2 else 'Y')
