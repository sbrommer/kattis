a, b, c = [int(n) for n in open(0).readlines()]

d = b ** 2 - 4 * a * c

print(2 if d > 0 else 1 if d == 0 else 0)
